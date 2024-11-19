from django.http import HttpResponse

def welcome(request):
    html_content = '''
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body style="text-align: center; font-family: Arial, sans-serif; margin-top: 50px;">
            <h1 style="color: #4CAF50;">Welcome to our app!!</h1>
            <div style="margin-top: 20px;">
                <a href="auth/login" style="text-decoration: none;">
                    <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #007BFF; border: none; border-radius: 5px; cursor: pointer;">
                        Login
                    </button>
                </a>
                <a href="auth/register" style="text-decoration: none; margin-left: 10px;">
                    <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #28A745; border: none; border-radius: 5px; cursor: pointer;">
                        Register
                    </button>
                </a>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html_content)
