#!/usr/bin/python
# -*- coding: utf-8 -*-
##
## admin.py for firl in /home/volent/dev/hfirl
## 
## Made by florent espanet
## Login   <espane_f@epitech.net>
## 
## Started on  Wed Nov 23 12:56:22 2011 florent espanet
## Last update Wed Nov 23 16:07:52 2011 yann vaillant
## Last update Wed Nov 23 14:39:15 2011 florent espanet
##

import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash

DATABASE = 'db/firl.db'
DEBUG = True
SECRET_KEY = 'we luvz python'
USERNAME = 'admin'
PASSWORD = 'admin'
