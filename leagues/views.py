from django.shortcuts import render, redirect
from django.db.models import Q
from .models import League, Team, Player
from . import team_maker


def index(request):
	return render(request, "leagues/index.html")


def all_data(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/data.html", context)


def make_data():
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")


def query_1(request):
	filter_leagues = League.objects.filter(sport="Baseball")
	teams = Team.objects.filter(league__sport__icontains="baseball")
	players = Player.objects.filter(curr_team__league__sport__icontains="baseball")

	context = {
		"leagues": filter_leagues,
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_2(request):
	filter_leagues = League.objects.filter(name__icontains="women")
	teams = Team.objects.filter(league__name__icontains="women")
	players = Player.objects.filter(curr_team__league__name__icontains="women")

	context = {
		"leagues": filter_leagues,
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_3(request):
	filter_leagues = League.objects.filter(name__icontains="hockey")
	teams = Team.objects.filter(league__sport__icontains="hockey")
	players = Player.objects.filter(curr_team__league__sport__icontains="hockey")

	context = {
		"leagues": filter_leagues,
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_4(request):
	filter_leagues = League.objects.exclude(name__icontains="football")
	teams = Team.objects.exclude(league__sport__icontains="football")
	players = Player.objects.exclude(curr_team__league__sport__icontains="football")

	context = {
		"leagues": filter_leagues,
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_5(request):
	filter_leagues = League.objects.filter(name__icontains="conference")
	teams = Team.objects.filter(league__sport__icontains="conference")
	players = Player.objects.filter(curr_team__league__sport__icontains="conference")

	context = {
		"leagues": filter_leagues,
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_6(request):
	filter_leagues = League.objects.filter(name__icontains="atlantic")
	teams = Team.objects.filter(league__sport__icontains="atlantic")
	players = Player.objects.filter(curr_team__league__sport__icontains="atlantic")

	context = {
		"leagues": filter_leagues,
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_7(request):
	teams = Team.objects.filter(location__icontains="dallas")
	players = Player.objects.filter(curr_team__location__icontains="dallas")

	context = {
		"leagues": "",
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_8(request):
	teams = Team.objects.filter(team_name__icontains="raptors")
	players = Player.objects.filter(curr_team__location__icontains="raptors")

	context = {
		"leagues": "",
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_9(request):
	teams = Team.objects.filter(location__icontains="city")
	players = Player.objects.filter(curr_team__location__icontains="city")

	context = {
		"leagues": "",
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_10(request):
	teams = Team.objects.filter(team_name__startswith="T")
	players = Player.objects.filter(curr_team__team_name__startswith="T")

	context = {
		"leagues": "",
		"teams": teams,
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_11(request):
	teams = Team.objects.all().order_by("location")

	context = {
		"leagues": "",
		"teams": teams,
		"players": "",
	}
	return render(request, "leagues/data.html", context)


def query_12(request):
	teams = Team.objects.all().order_by("-team_name")

	context = {
		"leagues": "",
		"teams": teams,
		"players": "",
	}
	return render(request, "leagues/data.html", context)


def query_13(request):
	players = Player.objects.filter(last_name__icontains="cooper")

	context = {
		"leagues": "",
		"teams": "",
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_14(request):
	players = Player.objects.filter(first_name__icontains="joshua")

	context = {
		"leagues": "",
		"teams": "",
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_15(request):
	players = Player.objects.filter(last_name__icontains="cooper").exclude(first_name__icontains="joshua")

	context = {
		"leagues": "",
		"teams": "",
		"players": players,
	}
	return render(request, "leagues/data.html", context)


def query_16(request):
	players = Player.objects.filter(Q(first_name__icontains="alexander") | Q(first_name__icontains="wyatt"))

	context = {
		"leagues": "",
		"teams": "",
		"players": players,
	}
	return render(request, "leagues/data.html", context)
