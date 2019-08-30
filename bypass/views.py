from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .run import make_bypass
from .run_fog import make_bypass_fog
from .massurl import mass_url
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from .atc import atc_driver
import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # 'cron'方式循环，周一到周五，每天9:30:10执行,id为工作ID作为标记
    # ('scheduler',"interval", seconds=1)  #用interval方式循环，每一秒执行一次
    @register_job(scheduler, 'cron', minute='25', id='task_time')
    def auto_bypass():
        if AutoBypass.objects.filter(bp_type='YS').first().is_on:
            t_now = time.localtime()
            bots = Bot.objects.all()
            count = bots.count()
            make_bypass(m=count)
            print(t_now)
        else:
            print('自动任务未开启')

    # 监控任务
    register_events(scheduler)
# 调度器开始
    scheduler.start()
except Exception as e:
    print(e)
# 报错则调度器停止执行
    scheduler.shutdown()

# Create your views here.


def index(request):
    key_list = Bypass.objects.filter(bot_type="YS")
    bot_list = Bot.objects.all()
    item_list = Item.objects.all()
    return render(request, 'index.html', locals())


def fog(request):
    key_list = Bypass.objects.filter(bot_type="Fog")
    bot_list = Bot.objects.all()
    item_list = Item.objects.all()
    return render(request, 'fog.html', locals())


def proxy(request):
    proxy_list = Proxies.objects.filter(bot_type="Fog")
    bot_list = Bot.objects.all()
    item_list = Item.objects.all()
    return render(request, 'proxy.html', locals())


@csrf_exempt
def button_bypass(request):
    if request.method == 'POST':
        post_content = request.POST
        post_id = post_content['id']
        if post_id == "#bp":
            # noinspection PyBroadException
            try:
                bots = Bot.objects.filter()
                count = bots.count()
                make_bypass(m=count)
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse({"success": False})
        elif post_id == "#fog-bp":
            # noinspection PyBroadException
            try:
                bots = FogBot.objects.all()
                count = bots.count()
                make_bypass_fog(m=count)
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse({"success": False})
        else:
            return JsonResponse({"success": False})

    else:
        return JsonResponse({"success": False})


@csrf_exempt
def mass_urls(request):

    if request.method == 'POST':

        post_content = request.POST
        post_id = post_content['id']

        post_url = post_content['url']
        if post_id == "#mass-url":
            # noinspection PyBroadException
            try:
                n = Bot.objects.count()
                mass_url(post_url, n)
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse({"success": False})
        elif post_id == "#fog-mass-url":
            # noinspection PyBroadException
            try:
                n = FogBot.objects.count()
                print(n)
                mass_url(post_url, n)
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse({"success": False})
    else:
        return JsonResponse({"success": False})


@csrf_exempt
def add_bot(request):
    if request.method == 'POST':
        post_content = request.POST
        post_id = post_content['id']
        print(post_id)
        if post_id == "#add-bot":
            bots = Bot.objects.all()
            count = bots.count()
            bot = Bot(bot_name='YS%s' % count, created_time=datetime.datetime.now(), bot_number=count, bot_type="YS")
            bp = Bypass(browser_name=bot.bot_name, bot_type="YS")
            bp.save()
            bot.save()
            return HttpResponse("success")
        elif post_id == "#fog-add-bot":
            print("fog added")
            bots = FogBot.objects.all()
            count = bots.count()
            bot = FogBot(bot_name='FOG%s' % count, created_time=datetime.datetime.now(), bot_number=count,
                         bot_type="Fog")
            bp = Bypass(browser_name=bot.bot_name, bot_type="Fog")
            bp.save()
            bot.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")


@csrf_exempt
def del_bot(request):
    if request.method == 'POST':
        post_content = request.POST
        post_id = post_content['id']
        if post_id == "#del-bot":
            bot = Bot.objects.filter(bot_type="YS").last()
            bp = Bypass.objects.filter(bot_type="YS").last()
            bot.delete()
            bp.delete()
            return HttpResponse("success")
        elif post_id == "#fog-del-bot":
            bot = FogBot.objects.filter(bot_type="Fog").last()
            bp = Bypass.objects.filter(bot_type="Fog").last()
            bot.delete()
            bp.delete()
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")


@csrf_exempt
def atc(request):
    if request.method == 'POST':
        print("atctest")
        post_content = request.POST
        url = post_content['url']
        # sizes = post_content['sizes']
        atc_driver(url)
        return HttpResponse("success")
    else:
        return HttpResponse("error")


@csrf_exempt
def check_auto_bp(request):
    post_content = request.POST
    post_id = post_content['id']
    if post_id == 'YS':
        auto_bp_task = AutoBypass.objects.filter(bp_type='YS').first()
        if auto_bp_task.is_on:
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    elif post_id == 'Fog':
        auto_bp_task = AutoBypass.objects.filter(bp_type='Fog').first()
        if auto_bp_task.is_on:
            return HttpResponse("success")
        else:
            return HttpResponse("error")


@csrf_exempt
def ys_autobp(request):
    post_content = request.POST
    post_id = post_content['id']
    ys_bp = AutoBypass.objects.get(bp_type='YS')
    if post_id == 'YSON':
        ys_bp.is_on = True
        ys_bp.save()
        return HttpResponse("success")
    elif post_id == 'YSOFF':
        ys_bp.is_on = False
        ys_bp.save()
        return HttpResponse("success")
    else:
        return HttpResponse("error")


def bypass_list(request):
    return HttpResponse('BYPASS状态')


def shop_monitor(request):
    return HttpResponse('YeezySupply监控')

