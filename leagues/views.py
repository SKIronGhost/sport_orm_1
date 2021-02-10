from django.shortcuts import render, redirect
from django.db.models import Q, Max
from .models import League, Team, Player
from . import team_maker
from django.db.models import Count, F


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


def query_17(request):
    teams = Team.objects.filter(league__name__icontains="atlantic soccer conference")
    context = {
        "leagues": "",
        "teams": teams,
        "players": "",
    }
    return render(request, "leagues/data.html", context)


def query_18(request):
    teams = Team.objects.filter(Q(team_name__icontains="penguins") & Q(location__icontains="boston"))
    players = Player.objects.filter(
        Q(curr_team__team_name__icontains="penguins") & Q(curr_team__location__icontains="boston"))
    context = {
        "leagues": "",
        "teams": teams,
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_19(request):
    leagues = League.objects.filter(name__icontains="International Collegiate Baseball Conference")
    players = Player.objects.filter(curr_team__league__name__icontains="International Collegiate Baseball Conference")
    context = {
        "leagues": leagues,
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_20(request):
    leagues = League.objects.filter(name__icontains="American Conference of Amateur Football")
    players = Player.objects.filter(Q(curr_team__league__name__icontains="American Conference of Amateur Football") & Q(
        last_name__icontains="lopez"))
    context = {
        "leagues": leagues,
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_21(request):
    players = Player.objects.filter(curr_team__league__sport__icontains="football")
    context = {
        "leagues": "",
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_22(request):
    filter_players = Player.objects.filter(first_name__icontains="sophia")
    team_id_set = []
    teams = []

    for team in filter_players.values():
        team_id_set.append(team['curr_team_id'])

    for i in team_id_set:
        teams.append(Team.objects.get(id=i))

    context = {
        "leagues": "",
        "teams": teams,
        "players": filter_players,
    }
    return render(request, "leagues/data.html", context)


def query_23(request):
    filter_players = Player.objects.filter(first_name__icontains="sophia")
    team_id_set = []
    teams = []
    league_id_set = []
    leagues = []

    for team_id in filter_players.values():
        team_id_set.append(team_id['curr_team_id'])

    for i in team_id_set:
        teams.append(Team.objects.get(id=i))

    for team in teams:
        league_id_set.append(team.league_id)
        print(league_id_set)

    for i in league_id_set:
        if i in leagues:
            break
        else:
            leagues.append(League.objects.get(id=i))
    print(leagues)

    context = {
        "leagues": leagues,
        "teams": teams,
        "players": filter_players,
    }
    return render(request, "leagues/data.html", context)


def query_24(request):
    players = Player.objects.filter(last_name__icontains="flores").exclude(
        curr_team__team_name__icontains="roughriders")
    context = {
        "leagues": "",
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_25(request):
    players = Player.objects.filter(first_name="Samuel", last_name="Evans")
    teams = Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.values()

    context = {
        "leagues": "",
        "teams": teams,
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_26(request):
    players = Team.objects.get(location="Manitoba", team_name="Tiger-Cats").all_players.values()

    context = {
        "leagues": "",
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_27(request):
    players_filter = Team.objects.get(location="Wichita", team_name="Vikings").all_players.all()
    players = players_filter.exclude(curr_team__team_name="Vikings", curr_team__location="Wichita")

    context = {
        "leagues": "",
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_28(request):
    jacob_gray = Player.objects.get(first_name="Jacob", last_name="Gray")
    teams = []
    for team in jacob_gray.all_teams.values():
        if "Colts" in team["team_name"] and "Oregon" in team["location"]:
            break
        else:
            teams.append(team)

    context = {
        "leagues": "",
        "teams": teams,
        "players": "",
    }
    return render(request, "leagues/data.html", context)


def query_29(request):
    players = Player.objects.filter(Q(first_name__icontains="joshua") & Q(
        all_teams__league__name__icontains="Atlantic Federation of Amateur Baseball Players"))

    context = {
        "leagues": "",
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)


def query_30(request):
    # teams_filter = Team.objects.filter(all_players__gt=11)
    teams = []
    for team in Team.objects.all():
        if len(team.all_players.all()) > 11:
            teams.append(team)
    # teams = Team.objects.filter(Count(F('all_players') > 11))
    context = {
        "leagues": "",
        "teams": teams,
        "players": "",
    }
    return render(request, "leagues/data.html", context)


def query_31(request):
    # {{player.all_teams.all.count}}
    players = Player.objects.annotate(max_teams=Count("all_teams")).order_by("max_teams")
    print(players)
    context = {
        "leagues": "",
        "teams": "",
        "players": players,
    }
    return render(request, "leagues/data.html", context)
