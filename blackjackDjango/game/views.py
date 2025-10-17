from django.shortcuts import render, redirect
from .blackjack import BlackjackGame

def get_game(request):
    data = request.session.get("game")
    if data:
        return BlackjackGame.from_dict(data)
    return BlackjackGame()

def save_game(request, game):
    request.session["game"] = game.to_dict()

def index(request):
    game = get_game(request)
    save_game(request, game)
    return render(request, "game/index.html", {"game": game.to_dict()})

def start_round(request):
    game = get_game(request)

    balance = request.POST.get("balance")
    if balance:
        game.balance = int(balance)

    bet = request.POST.get("bet")
    if not bet:
        return redirect("index")

    bet = int(bet)

    if not game.round_active:
        game.start_round(bet)
        save_game(request, game)

    return redirect("index")

def next_round(request):
    game = get_game(request)
    game.start_round(50)
    save_game(request, game)
    return redirect("index")

def hit(request):
    game = get_game(request)
    game.player_hit()
    save_game(request, game)
    return redirect("index")

def stay(request):
    game = get_game(request)
    game.player_stay()
    save_game(request, game)
    return redirect("index")

def double(request):
    game = get_game(request)
    game.player_double_down()
    save_game(request, game)
    return redirect("index")

def reset(request):
    request.session.flush()
    return redirect("index")
