from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security