# wp_ninja
This a simple tool to fully scan your WordPress site (themes, plugins, configurations...).
# What benefits do I can get by using it?
<ul>
  <li>Full Plugins and Themes scan which prides you with links to potential vulnerabilities in it.</li>
  <li>Full xmlrpc exploits check.</li>
  <li>Users enumeration.</li>
  <li>Users extraction from REST-API.</li>
  <li>Setting your own User-Agent.</li>
  <li>Setting your own Cookie.</li>
  <li>Setting your own HTTP proxy.</li>
  <li>Setting xmlrpc's path.</li>
  <li>Configurable Timeout.</li>
  <li>Disabling any undesirable scans.</li>
</ul>

# Installing:

<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">pip install -r requirements.txt
</pre></div>

# Usage examples:

<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">python wp_ninja.py -h
</pre></div>
<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">python wp_ninja.py -u http://www.example.com
</pre></div>
<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">python wp_ninja.py -u http://www.example.com -t 14 -ua "user agent string" -c "cookie string" -p "127.0.0.1:8080 -x /xmlrpc.php
</pre></div>
<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">python wp_ninja.py -d general -d xmlrpc -u http://www.example.com
</pre></div>

# Note:

<br>If you are using Windows OS, please install <a href="https://nodejs.org/en/download/">NodeJS</a> on your computer.
