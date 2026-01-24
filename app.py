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

@app.route("/callforpapers/submission-details")
def submission_details():
    return render_template("submission-details.html", active_page="callforpapers")

@app.route("/callforpapers/author-guidelines")
def author_guidelines():
    return render_template("author-guidelines.html", active_page="callforpapers")
@app.route("/callforpapers/review-process")
def review_process():
    return render_template("review-process.html", active_page="callforpapers")


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


@app.route("/committee")
def committee():
    committees = [
        {
            "title": "Chief Patron",
            "single": True,
            "members": [
                {
                    "name": "Shri. D. K. Mohan",
                    "designation": "Chairman, Cambridge Group of Institutions, Bengaluru, India",
                    "image": "/static/Images/patron.jpg"
                }
            ]
        },
        {
            "title": "Patrons",
            "single": True,
            "members": [
                {
                    "name": "Mr. Nithin Mohan",
                    "designation": "CEO, Cambridge Group of Institutions, Bengaluru, India",
                    "image": "/static/Images/CEO.jpg"
                }
            ]
        },
        {
            "title": "General Chair",
            "single": True,
            "members": [
                {
                    "name": "Dr. B V Ravishankar",
                    "designation": "Director / Principal, Cambridge Institute of Technology, Bengaluru, India",
                    "image": "/static/Images/GeneralChair.jpg"
                }
            ]
        },
        {
            "title": "Conference Chair",
            "single": True,
            "members": [
                {
                    "name": "Dr. Nagesh K. N",
                    "designation": "HoD (ECE), Vice Principal, CIT, Bengaluru, India",
                    "image": "/static/Images/nagesh.jpeg"
                }
            ]
        },
        {
            "title": "Organizing Chair and Co-ordinator",
            "members": [
                {
                    "name": "Dr. Ajay Kumar Dwivedi",
                    "designation": "Department R&D Head, Associate Professor, ECE, CIT, Bengaluru"
                },
                {
                    "name": "Dr. Vivek Singh",
                    "designation": "Associate Professor, ECE, CIT, Bengaluru"
                }
            ]
        },
        {
            "title": "Department Coordinator",
            "members": [
                {
                    "name": "Dr. Priya Singh",
                    "designation": "Assistant Professor, ECE, CIT, Bengaluru"
                },
                {
                    "name": "Dr. Indu K",
                    "designation": "Assistant Professor, ECE, CIT, Bengaluru"
                }
            ]
        },

        {
        "title": "Keynote Speaker",
        "members": [
            {
            "name": "Dr. Debabrata Das",
            "designation": "Chief Guest & Speaker, Director, IIIT Bangalore"
            },

            {
            "name": "Ms. Akansha Shukla",
            "designation": "Cyber Security Expert, ABN AMRO, Amsterdam, Netherlands"
            },
            {
            "name": "Dr. Nasimuddin",
            "designation": "Speaker, Scientist, A*STAR I2R Singapore"
            }
        ]
        },
        {
            "title": "International Advisory Committee",
            "members": [
                {"name": "Dr. Sanjeet Dwivedi", "designation": "Senior R&D Control Engineer, Danfoss Power Electronics, Denmark"},
                {"name": "Prof. Ramesh Bansal", "designation": "University of Pretoria, South Africa"},
                {"name": "Prof. Vincenzo Piuri", "designation": "University of Milan, Italy"},
                {"name": "Prof. Giuseppe Buja", "designation": "University of Padova, Italy"},
                {"name": "Prof. Tarlochan S Sidhu", "designation": "Ontario Tech University, Canada"},
                {"name": "Dr. Saurabh Singh", "designation": "Dongguk University, South Korea"},
                {"name": "Dr. Joshua Thomas", "designation": "UOW Malaysia KDU, Penang"},
                {"name": "Dr. Deepak Kumar Jain", "designation": "Chongqing University, China"},
                {"name": "Dr. Ashutosh Mishra", "designation": "Yonsei University, South Korea"},
                {"name": "Dr. Udaya Dampage", "designation": "Kotelawala Defence University, Sri Lanka"},
                {"name": "Dr. Satyendra Kumar Mishra", "designation": "Laval University, Canada"},
                {"name": "Dr. Tawfik Ismail", "designation": "Nile University, Egypt"},
                {"name": "Dr. Santosh Kumar", "designation": "Liaocheng University, China"},
                {"name": "Prof Selwyn Piramuthu", "designation": "University of Florida,USA"},
                {"name": "Prof. Sarangapani Jagannathan", "designation": "Missouri S&T, USA"},
                {"name": "Dr. Alexey Nazarov", "designation": "Faculty of Computer Science Higher School of Economics, National Research University, Moscow, Russia."},
                {"name": "Dr. Nizar Al Bassam", "designation": "Center for Research and Consultancy, Middle East College, Muscat"},
                {"name": "Dr. Arun Shivashankarappa Nagarle", "designation": "Department of Planning and Development, Department of Computing, Middle East College, Muscat"},
                {"name": "Dr. Mounir Dhibi", "designation": "Department of Computing, Middle East College, Muscat"},
                {"name": "Dr. Vishal Dattana", "designation": "Department of Computing, Middle East College, Muscat"}

                
            ]
        },

        {
        "title": "National Advisory Committee",
        "members": [
            {
            "name": "Dr. G. K. Vishwakarma",
            "designation": "IIT Dhanbad, India"
            },
            {
            "name": "Dr. Manish Goswami",
            "designation": "Electronics and Communication Engineering, IIIT Allahabad, India"
            },
            {
            "name": "Prof. Satyabrata Jit",
            "designation": "Department of Electronics Engineering, IIT BHU, India"
            },
            {
            "name": "Prof. D. P. Mishra",
            "designation": "Department of Aerospace Engineering, IIT Kanpur, India"
            },
            {
            "name": "Prof. Ravi Prakash",
            "designation": "Mechanical Engineering, MNNIT Allahabad, India"
            },
            {
            "name": "Dr. Mushtaq Ahmed",
            "designation": "Department of Computer Science and Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Dr. Namita Mittal",
            "designation": "Department of Computer Science and Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Prof. K. K. Sharma",
            "designation": "Electronics and Communication Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Prof. Rajendra Prasad Yadav",
            "designation": "Electronics and Communication Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Prof. Ghanshyam Singh",
            "designation": "Electronics and Communication Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Dr. Tarun Varma",
            "designation": "Electronics and Communication Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Dr. R. K. Pateriya",
            "designation": "Department of Computer Science and Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Dr. Ajay Somkuwar",
            "designation": "Department of Computer Science and Engineering, MNIT Jaipur, India"
            },
            {
            "name": "Dr. Ashutosh Kumar Singh",
            "designation": "Department of Computer Science and Engineering, NIT Kurukshetra, India"
            },
            {
            "name": "Dr. Brahmjit Singh",
            "designation": "Electronics and Communication Engineering, NIT Kurukshetra, India"
            },
            {
            "name": "Dr. R. K. Sharma",
            "designation": "Electronics and Communication Engineering, NIT Kurukshetra, India"
            },
            {
            "name": "Dr. O. P. Sahu",
            "designation": "Electronics and Communication Engineering, NIT Kurukshetra, India"
            },
            {
            "name": "Dr. Vrinda Gupta",
            "designation": "Electronics and Communication Engineering, NIT Kurukshetra, India"
            },
            {
            "name": "Dr. Vikas Mittal",
            "designation": "Electronics and Communication Engineering, NIT Kurukshetra, India"
            },
            {
            "name": "Dr. Maheshwari Prasad Singh",
            "designation": "Department of Computer Science and Engineering, NIT Patna, India"
            },
            {
            "name": "Dr. Ravi Bhushan Mishra",
            "designation": "Department of Computer Science and Engineering, NIT Patna, India"
            },
            {
            "name": "Dr. Ritesh Kumar Mishra",
            "designation": "Electronics and Communication Engineering, NIT Patna, India"
            },
            {
            "name": "Prof. Mahua Bhattacharya",
            "designation": "Information Technology, IIIT Gwalior, India"
            },
            {
            "name": "Dr. Peddoju Sateesh Kumar",
            "designation": "Department of Computer Science and Engineering, IIT Roorkee, India"
            },
            {
            "name": "Prof. Kaushal Kumar Shukla",
            "designation": "Department of Computer Science and Engineering, IIT BHU, Varanasi, India"
            },
            {
            "name": "Dr. Navin Singh Rajput",
            "designation": "Electronics and Communication Engineering, IIT BHU, Varanasi, India"
            },
            {"name": "Prof. Satyabrata Jit",
            "designation": "Electronics and Communication Engineering, IIT BHU, Varanasi, India"    
            },
            {
            "name": "Dr. Ashish Khare",
            "designation": "Electronics and Communication Engineering, University of Allahabad, India"
            },
            {
            "name": "Dr. Rajneesh Kumar Srivastava",
            "designation": "Electronics and Communication Engineering, University of Allahabad, India"
            },
            {
            "name": "Dr. Arun Prakash",
            "designation": "Electronics and Communication Engineering, MNNIT Allahabad, India"
            },
            {
            "name": "Dr. Tanveer Siddiqui",
            "designation": "Electronics and Communication Engineering, University of Allahabad, India"
            },
            {
            "name": "Dr. Sanjai Singh",
            "designation": "Electronics and Communication Engineering, IIIT Allahabad, India"
            },
            {
            "name": "Dr. D. Kannadassan",
            "designation": "Prof and Head, DCE, VIT, Vellore"
            }
        ]
        },

        {
            "title": "Technical Program Committee",
            "members": [
                {"name": "Dr. Arun Prakash", "designation": "Electronics and Communication Engineering, MNNIT Allahabad, India"},
                {"name": "Dr. Rajiv Singh", "designation": "Electrical Engineering, GBPUA&T Pant Nagar, India"},
                {"name": "Dr. Anand Sharma", "designation": "Electronics and Communication Engineering, MNNIT Allahabad, India"},
                {"name": "Dr. Somak Bhattacharya", "designation": "Electronics Engineering, IIT BHU, India"},
                {"name": "Dr. Triloki Pant", "designation": "Information Technology, IIIT Allahabad, India"},
                {"name": "Dr. Sudhakar Singh", "designation": "Electronics and Communication Engineering, University of Allahabad, India"},
                {"name": "Dr. Richa Mishra", "designation": "Electronics and Communication Engineering, University of Allahabad, India"},
                {"name": "Dr. Sudhanshu Kumar Jha", "designation": "Electronics and Communication Engineering, University of Allahabad, India"},
                {"name": "Dr. Vibhu Srivastava", "designation": "Electronics and Communication Engineering, REVA University, Bengaluru, India"},
                {"name": "Dr. Pinku Ranjan", "designation": "Electronics and Communication Engineering, ABVIIIT Gwalior, India"},
                {"name": "Dr. Manoj Tolai", "designation": "Electronics and Communication Engineering, Atrai IT, Bengaluru, India"},
                {"name": "Dr. K. Raja", "designation": "Computer Science and Engineering, SRM Institute of Science & Technology, Chennai, India"},
                {"name": "Dr. Praveen Joe I. R.", "designation": "Computer Science and Engineering, Vellore Institute of Technology, Chennai, India"},
                {"name": "Dr. L. Sharmila", "designation": "Computer Science and Engineering, Agni College of Technology, Chennai, India"},
                {"name": "Dr. A. Rajasekar", "designation": "Computer Science and Engineering, Dhaanish Ahmed College of Engineering, Chennai, India"},
                {"name": "Dr. Sivaram Rajeyyagari", "designation": "Computer Science and Engineering, Saudi Arabia"},
                {"name": "Dr. Arumugam", "designation": "Computer Science and Engineering, Saveetha School of Engineering, Chennai, India"},
                {"name": "Dr. Ahmad Tasnim Siddiqui", "designation": "Computer Science and Engineering, Sherwood Educational Group, Lucknow, India"},
                {"name": "Dr. Muzamil Hussain", "designation": "Computer Science and Engineering, Saudi Arabia"},
                {"name": "Dr. Syed Naimatullah Hussain", "designation": "Computer Science and Engineering, NCET Bengaluru, India"},
                {"name": "Dr. Anil Kannur", "designation": "Computer Science and Engineering, NCET Bengaluru, India"},
                {"name": "Dr. Sonali Agarwal", "designation": "Information Technology, IIIT Allahabad, India"},
                {"name": "Dr. Shiv Ram Dubey", "designation": "Information Technology, IIIT Allahabad, India"},
                {"name": "Dr. Anjali Gautam", "designation": "Information Technology, IIIT Allahabad, India"},
                {"name": "Dr. Mohammed Javed", "designation": "Information Technology, IIIT Allahabad, India"},
                {"name": "Dr. Rahul Kala", "designation": "Information Technology, IIIT Allahabad, India"},
                {"name": "Dr. Himanshu Maurya", "designation": "Electronics and Communication Engineering, IIIT Allahabad, India"},
                {"name": "Dr. Guruprasad S.", "designation": "Electronics and Communication Engineering, Sri Siddhartha Institute of Technology, Karnataka, India"},
                {"name": "Dr. G. Pradeep", "designation": "Electronics and Communication Engineering, Vignan Institute of Technology and Research, Guntur, India"},
                {"name": "Dr. Chandrashekar H. M.", "designation": "Electronics and Communication Engineering, Sri Siddhartha Institute of Technology, Karnataka, India"},
                {"name": "Dr. M. Bharathraj Kumar", "designation": "Electronics and Communication Engineering, SDMIT Ujire, India"},
                {"name": "Dr. Srinidhi G. A.", "designation": "Electronics and Communication Engineering, KLE Technological University, Hubli, India"},
                {"name": "Dr. Kallinatha H. D.", "designation": "Computer Science and Engineering, Sri Siddhartha Institute of Technology, Karnataka, India"},
                {"name": "Dr. Basavaraju K. S.", "designation": "Electronics and Communication Engineering, NITK Surathkal, India"},
                {"name": "Dr. Sandeep M.", "designation": "Computer Science and Engineering, Government Engineering College Chamarajanagar, India"},
                {"name": "Dr. Pooja Mishra", "designation": "Electronics and Communication Engineering, IIIT Allahabad, India"},
                {"name": "Dr. Bhawana Rudra", "designation": "Information Technology, NITK Surathkal, India"},
                {"name": "Dr. Kiran M.", "designation": "Information Technology, NITK Surathkal, India"},
                {"name": "Dr. Dinesh Naik", "designation": "Information Technology, NITK Surathkal, India"},
                {"name": "Dr. B. R. Chandavarkar", "designation": "Computer Science and Engineering, NITK Surathkal, India"},
                {"name": "Dr. Biswajit R. Bhowmik", "designation": "Computer Science and Engineering, NITK Surathkal, India"},
                {"name": "Dr. Rajiv Singh", "designation": "Computer Science and Engineering, Banasthali Vidyapith, Rajasthan, India"},
                {"name": "Dr. Manju Khari", "designation": "Computer Science and Engineering, AIACTR Delhi, India"},
                {"name": "Dr. Vikash Kumar Mishra", "designation": "Computer Science and Engineering, Galgotias College of Engineering and Technology, Greater Noida, India"},
                {"name": "Dr. Manoj Diwarkar", "designation": "Computer Science and Engineering, Graphic Era Deemed University, Dehradun, India"},
                {"name": "Dr. Radhika Gour", "designation": "Electronics and Communication Engineering, IIIT Allahabad, India"},
                {"name": "Dr. Shanti Chandra", "designation": "Electronics and Communication Engineering, IIIT Allahabad, India"},
                {"name": "Dr. Satheesha T. Y.", "designation": "Electronics and Communication Engineering, SOET CMR University, Bengaluru, India"},
                {"name": "Dr. S. Saravana Kumar", "designation": "Computer Science and Engineering, SOET CMR University, Bengaluru, India"},
                {"name": "Dr. Mala Kalra", "designation": "Computer Science and Engineering, NITTTR Chandigarh, India"},
                {"name": "Dr. Shano Solanki", "designation": "Computer Science and Engineering, NITTTR Chandigarh, India"},
                {"name": "Dr. Abdul Aleem", "designation": "Computer Science and Engineering, Galgotias University, Greater Noida, India"},
                {"name": "Dr. Prashant Srivastava", "designation": "Computer Science and Engineering, SIET Prayagraj, India"},
                {"name": "Dr. Abhishek Kumar", "designation": "Electronics and Communication Engineering, SOET CMR University, Bengaluru, India"},
                {"name": "Dr. Arun Balodi", "designation": "Electronics and Communication Engineering, Dayanand Sagar University, Bengaluru, India"}
            ]
        },

        {
            "title": "Industry Advisory Committee",
            "members": [
                {"name": "Dr. Hema Singh", "designation": "Chief Scientist & Head, Centre for Electromagnetics (CEM), CSIR-NAL, Bangalore, India"},
                {"name": "Dr. V. S. Gangwar", "designation": "Senior Scientist (Scientist 'F'), LRDE, Bangalore, India"},
                {"name": "Ms. Vineetha Joy", "designation": "Senior Scientis, CSIR-NAL, Bangalore, India"},
                {"name": "Dr. Puneet Kumar Mishra", "designation": "Scientist, URSC, Bengaluru , India"},
            ]
        },
        {
        "title": "Publicity Chair",
        "members": [
            {
            "name": "Dr. Chrispin Jiji",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Lakshmi C. R.",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Hariprasad T. L.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mrs. Chaithra S.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Jayaprakash S.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Athul Ghosh P.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Praveen Kumar K. C.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            }
        ]
        },
        {
        "title": "Local Organizing Committee",
        "members": [
            {
            "name": "Dr. Shiva Panchakshari T. G.",
            "designation": "Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Kavitha M. V.",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Ravi Kumar M.",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mrs. Shakila D.",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Veerappa S. C.",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. A. M. Lokesh",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mrs. Roopa M.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Shyam Sundar V.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mrs. Nandini Kumar B.",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Mr. Malikarjun Hampali",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Jaya Chandwani",
            "designation": "Assistant Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Girish H.",
            "designation": "Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Bitan De",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Srinivasalu G.",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Shivananda",
            "designation": "Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            },
            {
            "name": "Dr. Trinath Reddy",
            "designation": "Associate Professor, Electronics and Communication Engineering, Cambridge Institute of Technology, Bengaluru, India"
            }
        ]
        }
    ]

    return render_template("committee.html", committees=committees)


if __name__ == "__main__":
    app.run(debug=True)
