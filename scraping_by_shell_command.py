import subprocess
import sys
cmd = "wget https://www.amazon.co.jp/rss/new-releases/dvd/896246 -o;cat ./www.amazon.co.jp/rss/new-releases/dvd/896246 | grep -E -o '<span class=\"riRssContributor\">.+?<span class=\"byLinePipe\">'|awk '{gsub(/<[^<]*>/,\"\");print}'"
proc = subprocess.Popen(
    cmd,
    shell  = True,                            #シェル経由($ sh -c "command")で実行。
    stdin  = subprocess.PIPE,                 #1
    stdout = subprocess.PIPE,                 #2
    stderr = subprocess.PIPE)                 #3
stdout_data, stderr_data = proc.communicate() #処理実行を待つ(†1)
sys.stdout.buffer.write(stdout_data)