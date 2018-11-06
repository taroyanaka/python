#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import sys
cmd = "wget https://www.amazon.co.jp/rss/new-releases/dvd/896246 ; cat ./896246 | grep -E -o '<span class=\"riRssContributor\">.+?<span class=\"byLinePipe\">'|awk '{gsub(/<[^<]*>/,\"\");print}'"

proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(stdout_data, stderr_data) = proc.communicate()

sys.stdout.buffer.write(stdout_data)