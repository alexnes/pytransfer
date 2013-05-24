#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from flask import Flask, render_template, request, Response
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from stations import station, username, password, remote_path, local_path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		filename = request.form["filename"]
		st_id = request.form["station_id"]

		ssh = SSHClient()
		ssh.set_missing_host_key_policy(AutoAddPolicy())
		ssh.load_system_host_keys()
		ssh.connect(station[st_id]["ip"], username=username, password=password)

		try:
			scp = SCPClient(ssh.get_transport())
			scp.get(remote_path + filename, local_path=local_path)
		except:
			ssh.close()
			return render_template('index.html', stations=station, error=u"ошибка при получении файла")

		ssh.close()		

		return flask.send_file(local_path + filename, mimetype='text/csv', as_attachment=True, attachment_filename=filename)

	else:
		return render_template('index.html', stations=station)

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=8088)