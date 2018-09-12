#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from flask import Flask, render_template_string, jsonify
app = Flask(__name__)

import logging
logging.basicConfig(level=logging.DEBUG)

# Для импорта common.py
import sys
sys.path.append('..')

from common import generate_table


@app.route("/")
def index():
    return render_template_string("""\
<html>
<head>
    <meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
    <script type="text/javascript" src="{{ url_for('static', filename='js/jquery-3.1.1.min.js') }}"></script>
    <title>generate_table</title>
    
    <style>
        table {
            border-spacing: 0;
        }
        
        table, th, td {
           border: solid black 1px;
        }
    
        td {
            width: 30px;
            padding: 5px;
        }
        
        tr:nth-child(1) {
            background: #cccccc;
        }
        tr > td:nth-child(1) {
            background: #cccccc;
        }
        tr:nth-child(1) > td:nth-child(1) {
            background: #ffffff;
        }
        
    </style>
</head>
<body>
    <script>
        $(document).ready(function() {
            console.log("call get_table()");

            $.ajax({
                url: "/get_table",
                dataType: "json",  // тип данных загружаемых с сервера

                success: function(data) {
                    console.log("success");
                    console.log(data);
                    
                    var table = $('<table>');
                    $('body').append(table);
                    
                    for (var i = 0; i < data.length; i++) {
                        var tr = $('<tr>');
                        var row = data[i];
                        
                        for (var j = 0; j < row.length; j++) {
                            var td = $('<td>');
                            td.text(row[j]);
                            
                            tr.append(td);
                        }
                        
                        table.append(tr);
                    }
                    
                    // $('#out_get_text').text(JSON.stringify(data));
                },

                error: function(data) {
                    console.log("error");
                    console.log(data);
                }
            });
        });
    </script>
    
</body>
</html>
    """)


@app.route("/get_table")
def get_table():
    items = generate_table(10)

    return jsonify(items)


if __name__ == '__main__':
    app.debug = True

    # Localhost
    # port=0 -- random free port
    # app.run(port=0)
    app.run(
        port=5000,

        # :param threaded: should the process handle each request in a separate
        #                  thread?
        # :param processes: if greater than 1 then handle each request in a new process
        #                   up to this maximum number of concurrent processes.
        threaded=True,
    )

    # # Public IP
    # app.run(host='0.0.0.0')
