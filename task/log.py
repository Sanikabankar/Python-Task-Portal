# from flask import Flask, redirect,request,Response,url_for,session

# app=Flask(__name__)
# app.secret_key = "supersecrete"

# @app.route("/", methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         name=request.form.get("name")
#         pass1=request.form.get("pass1")

#         if name=="pallavi" and pass1=="124":
#             session["user"]=name
#             return redirect(url_for("welcome")) 
#         else:
#             return Response("Invalid",mimetype="text/plain")
        
#     return '''
#     <h2>Welcome</h2>
#     <form method="POST">
#     name:<input type="text" name="name"><br>
#     pass:<input type="password" name="pass1"><br>
#     <input type="submit" value="login">
#     </form>
#     '''


# @app.route("/welcome")
# def welcome():
#     if "user" in session:
#         return f'''
#         <h2>Welcome, {session["user"]}!</h2>
#         <a href="{url_for('logout')}">logout</a>
#         '''
#     return redirect(url_for("login"))

# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect(url_for("login"))

from flask import Flask, redirect, request, Response, url_for, session

app = Flask(__name__)
app.secret_key = "supersecrete"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        pass1 = request.form.get("pass1")

        if name == "pallavi" and pass1 == "124":
            session["user"] = name
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid", mimetype="text/plain")
        
    return '''
    <h2>Welcome</h2>
    <form method="POST">
        name: <input type="text" name="name"><br>
        pass: <input type="password" name="pass1"><br>
        <input type="submit" value="login">
    </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
