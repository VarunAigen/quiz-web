def get_questions():
    return [
        {
            'id': 1,
            'question': "What is Flask?",
            'choices': [
                "A full-stack web framework",
                "A micro web framework",
                "A JavaScript framework",
                "None of the above"
            ],
            'answer': "A micro web framework"
        },
        {
            'id': 2,
            'question': "Which of the following is used to run a Flask application?",
            'choices': [
                "Flask.run()",
                "Flask.start()",
                "Flask.serve()",
                "Flask.execute()"
            ],
            'answer': "Flask.run()"
        },
        {
            'id': 3,
            'question': "Which templating engine does Flask use by default?",
            'choices': [
                "Jinja2",
                "Mako",
                "Cheetaht",
                "Django Templates"
            ],
            'answer': "Jinja2"
        },
        {
            'id': 4,
            'question': "What is the purpose of the @app.route() decorator in Flask?",
            'choices': [
                "To define the Flask app",
                "To define a URL route that maps to a view function",
                "To connect the database to Flask",
                "To run the Flask application"
            ],
            'answer': "To define a URL route that maps to a view function"
        },
        {
            'id': 5,
            'question': "Which Flask extension can you use for working with forms?",
            'choices': [
                "Flask-Form",
                "Flask-WTF",
                "Flask-HTML",
                "Flask-Forms"
            ],
            'answer': "Flask-WTF"
        },
        {
            'id': 6,
            'question': "How do you define a route that only accepts POST requests in Flask?",
            'choices': [
                "@app.route('/example', methods=['GET', 'POST'])",
                "@app.route('/example', methods=['POST'])",
                "@app.route('/example', post=True)",
                "@app.post('/example')"
            ],
            'answer': "@app.route('/example', methods=['POST'])"
        },
        {
            'id': 7,
            'question': "What is the purpose of Flask's `request` object?",
            'choices': [
                "To handle all HTTP requests",
                "To parse form data and retrieve URL parameters",
                "To define the response of the app",
                "To validate user input"
            ],
            'answer': "To parse form data and retrieve URL parameters"
        },
        {
            'id': 8,
            'question': "What is the role of the `Flask` class in a Flask application?",
            'choices': [
                "It initializes the web application",
                "It runs the server",
                "It defines the routes",
                "It handles HTTP requests"
            ],
            'answer': "It initializes the web application"
        },
        {
            'id': 9,
            'question': "Which Flask extension is commonly used to add database support?",
            'choices': [
                "Flask-RESTful",
                "Flask-SQLAlchemy",
                "Flask-Migrate",
                "Flask-Mail"
            ],
            'answer': "Flask-SQLAlchemy"
        },
        {
            'id': 10,
            'question': "How do you run a Flask application in development mode with debugging enabled?",
            'choices': [
                "app.run(debug=True)",
                "app.run(debug=False)",
                "app.start(debug=True)",
                "Flask.run(debug=True)"
            ],
            'answer': "app.run(debug=True)"
        },
        {
            'id': 11,
            'question': "What is the default host and port for a Flask app when running locally?",
            'choices': [
                "localhost:8000",
                "127.0.0.1:5000",
                "localhost:5000",
                "0.0.0.0:5000"
            ],
            'answer': "127.0.0.1:5000"
        },
        {
            'id': 12,
            'question': "Which function is used to render HTML templates in Flask?",
            'choices': [
                "render_template()",
                "render_html()",
                "template.render()",
                "generate_html()"
            ],
            'answer': "render_template()"
        },
        {
            'id': 13,
            'question': "How do you access URL parameters in Flask?",
            'choices': [
                "request.form['param_name']",
                "request.args['param_name']",
                "request.url['param_name']",
                "request.parameters['param_name']"
            ],
            'answer': "request.args['param_name']"
        },
        {
            'id': 14,
            'question': "What does the `@app.route('/')` decorator define in Flask?",
            'choices': [
                "A home page for your website",
                "A route for handling HTTP POST requests",
                "A route for HTTP GET requests to the root URL",
                "None of the above"
            ],
            'answer': "A route for HTTP GET requests to the root URL"
        }
    ]
