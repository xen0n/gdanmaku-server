#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from flask import render_template
from flask import request, g, Response
import gevent

from . import app

new_danmaku = gevent.event.Event()
danmaku_channels = {
    "default": []
}


@app.route("/channel/<cname>", methods=["GET"])
def channel_view(cname):
    cm = g.channel_manager

    channel = cm.get_channel(cname)
    token = channel.gen_web_token()
    if channel is None:
        return "Not Found", 404

    return render_template("channel.html", channel=channel, token=token)


@app.route("/", methods=["GET"])
def index():
    channels = g.channel_manager.channels(instance=True)
    return render_template("index.html", channels=channels)


@app.route("/channel-new/", methods=["GET"])
def channel_create():
    return render_template("new_channel.html")

# vim: ts=4 sw=4 sts=4 expandtab
