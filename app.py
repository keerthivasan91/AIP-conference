from flask import Flask, render_template, request, flash
import os
from flask_mail import Mail, Message # type: ignore

registration_fees = [
    {
        "category": "Research Scholar / UG / PG (Only)",
        "national": "₹10,000",
        "international": "$200"
    },
    {
        "category": "Faculties / Scientists",
        "national": "₹12,000",
        "international": "$300"
    },
    {
        "category": "Industry Person",
        "national": "₹14,000",
        "international": "$400"
    }
]

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

@app.route('/')
def home():
    return render_template('index.html',active_page='home')

@app.route('/about')
def about():
    return render_template('about.html',active_page='about')

@app.route('/registration')
def registration():
    return render_template('registration.html',active_page='registration', fees=registration_fees)

@app.route('/venue')
def venue():
    return render_template('venue.html',active_page='venue')

@app.route('/submitpaper')
def submitpaper():
    return render_template('submitpaper.html',active_page='submitpaper')

@app.route('/callforpapers/submission-guidelines')
def submission_guidelines():
    return render_template(
        'submission-guidelines.html',
        active_page='submission-guidelines'
    )

@app.route('/callforpapers/conference-track')
def conference_track():
    return render_template(
        'conference-track.html',
        active_page='conference-track'
    )

@app.route('/UTCA2023')
def UTCA2023():
    return render_template('UTCA2023.html',active_page='UTCA2023')

'''@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name') or "Anonymous"
        email = request.form.get('email') or "Not provided"
        message_content = request.form.get('message') or "No message"

        recipient = os.getenv("MAIL_USERNAME")
        if not recipient:
            flash("Mail username not configured!", "error")
            return render_template('contact.html', success=False, active_page='contact')

        msg = Message(
            subject=f"New Contact Form Message from {name}",
            recipients=[recipient]
        )
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"


    return render_template('contact.html', success=None, active_page='contact')'''

@app.route("/contact")
def contact():
    return render_template("contact.html", active_page="contact")


@app.route("/committee")
def committee():
    return render_template("committee.html", active_page="committee")


@app.route("/iskcon-bangalore")
def iskcon_bangalore():
    return render_template("iskcon-bangalore.html", active_page="iskcon-bangalore")

@app.route("/nandi-hills")
def nandi_hills():
    return render_template("nandi-hills.html", active_page="nandi-hills")


@app.route("/vidhana-soudha")
def vidhana_soudha():   
    return render_template("vidhana-soudha.html", active_page="vidhana-soudha") 


@app.route("/bangalore-palace")
def bangalore_palace():   
    return render_template("bangalore-palace.html", active_page="bangalore-palace")

@app.route("/lalbagh")
def lalbagh():   
    return render_template("lalbagh.html", active_page="lalbagh")   

if __name__ == "__main__":
    app.run(debug=True)
