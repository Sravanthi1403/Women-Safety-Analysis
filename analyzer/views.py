import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
import numpy as np
import pickle
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

MODEL_PATH = os.path.join(settings.BASE_DIR, 'models/bilstm_model.h5')
TOKENIZER_PATH = os.path.join(settings.BASE_DIR, 'models/bilstm_tokenizer.pkl')

model = load_model(MODEL_PATH)

with open(TOKENIZER_PATH, 'rb') as f:
    tokenizer = pickle.load(f)

MAX_LEN = 60


# ==============================
# SAME CLEANING USED IN TRAINING
# ==============================

URL_RE = re.compile(r'https?://\S+|www\.\S+')
MENTION_RE = re.compile(r'@\w+')
HASHTAG_RE = re.compile(r'#')
MULTISPACE = re.compile(r'\s+')


def clean_text_dl(text):
    if not isinstance(text, str):
        return ""

    text = text.strip()
    text = URL_RE.sub(' ', text)
    text = MENTION_RE.sub(' ', text)
    text = HASHTAG_RE.sub('', text)
    text = MULTISPACE.sub(' ', text).strip()

    return text


def home(request):
    return render(request, "home.html")


@login_required
def predict(request):

    prediction = None

    if request.method == "POST":

        text_input = request.POST.get("text_input")

        # Apply same preprocessing used during training
        text_input = clean_text_dl(text_input)

        # Convert to sequence
        sequence = tokenizer.texts_to_sequences([text_input])

        # SAME padding used during training
        padded_sequence = pad_sequences(
            sequence,
            maxlen=MAX_LEN,
            padding='post',
            truncating='post'
        )

        # Predict
        result = model.predict(
            padded_sequence,
            verbose=0
        )

        predicted_class = np.argmax(result, axis=1)[0]

        print("===================================")
        print("User Input :", text_input)
        print("Raw Prediction :", result)
        print("Predicted Index :", predicted_class)
        print("Django Tokenizer Size :", len(tokenizer.word_index))
        print("Django Sequence :", sequence)
        print("===================================")

        if predicted_class == 0:
            prediction = "Negative"

        elif predicted_class == 1:
            prediction = "Neutral"

        else:
            prediction = "Positive"

    return render(request, "predict.html", {"prediction": prediction})


@login_required
def analytics(request):
    return render(request, 'analytics.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            messages.error(request, "Wrong username or password")

    return render(request, "login.html")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect("register")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            return redirect("register")

        if not re.search("[A-Z]", password):
            messages.error(request, "Password must include a capital letter")
            return redirect("register")

        if not re.search("[a-z]", password):
            messages.error(request, "Password must include a small letter")
            return redirect("register")

        if not re.search("[0-9]", password):
            messages.error(request, "Password must include a number")
            return redirect("register")

        if not re.search("[@#$%^&+=!]", password):
            messages.error(request, "Password must include special symbol")
            return redirect("register")

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return redirect("/")