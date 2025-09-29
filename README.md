# 🚀 Personal Portfolio Website

A modern, professional portfolio website built with Flask and featuring a sleek glass morphism design.

## 🌐 **Live Website Preview**

### 📱 **Portfolio Pages**

| Page | Description | Direct Link |
|------|-------------|-------------|
| 🏠 **Home** | Professional landing page with glass morphism design | [View Home Page](frontend/index.html) |
| 👨‍💻 **About Me** | Personal introduction and professional background | [View About Page](frontend/about.html) |
| 🛠️ **Technical Skills** | Comprehensive technical skills showcase | [View Skills Page](frontend/technicalSkills.html) |
| 🎓 **Education** | Educational background and qualifications | [View Education Page](frontend/education.html) |
| 💼 **Projects** | Portfolio of completed projects and applications | [View Projects Page](frontend/projects.html) |
| 🏆 **Certifications** | Professional certifications and achievements | [View Certifications Page](frontend/certifications.html) |

## ✨ **Quick Navigation**

- 🏠 **[Home](frontend/index.html)** - Landing page
- 👨‍💻 **[About Me](frontend/about.html)** - Personal introduction
- 🛠️ **[Technical Skills](frontend/technicalSkills.html)** - Skills showcase
- 🎓 **[Education](frontend/education.html)** - Educational background
- 💼 **[Projects](frontend/projects.html)** - Project portfolio
- 🏆 **[Certifications](frontend/certifications.html)** - Professional certifications

## 🎨 **Design Features**

- **Glass Morphism Effects** - Modern frosted glass design
- **Professional Gradients** - Beautiful color schemes
- **Responsive Layout** - Works on all devices
- **Smooth Animations** - Hover effects and transitions
- **Clean Typography** - Professional, readable fonts

## 🛠️ **Technology Stack**

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3
- **Styling**: Custom CSS with glass morphism
- **Server**: Flask development server

## 📁 **Project Structure**

```
Portfolio/
├── backen/
│   └── backend.py              # Flask application
├── frontend/
│   ├── index.html             # Home page
│   ├── about.html             # About Me page
│   ├── technicalSkills.html   # Technical Skills page
│   ├── education.html         # Education page
│   ├── projects.html          # Projects page
│   ├── certifications.html    # Certifications page
│   └── style/                 # CSS stylesheets
│       ├── Home.css
│       ├── about.css
│       ├── technicalSkills.css
│       ├── Education.css
│       ├── projects.css
│       └── certification.css
└── README.md
```

## 🚀 **Getting Started**

### Prerequisites
- Python 3.x
- pip3

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Heisenberg2005-glich/Personal-Portfolio.git
   cd Personal-Portfolio
   ```

2. **Install dependencies**
   ```bash
   pip3 install flask flask-cors
   ```

3. **Run the application**
   ```bash
   cd backen
   python3 backend.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5004/`

## 💼 **Featured Projects**

### 🏦 **SecureBank – Online Banking Management System**
- **Technologies**: Django, Python, PostgreSQL, HTML/CSS, JavaScript
- **Features**: User authentication, account management, transaction history
- **Description**: A secure banking application with modern UI and robust security features

### 🤖 **TradeSmart – AI-Powered Trading Platform**
- **Technologies**: Python, Machine Learning, Flask, React
- **Features**: AI predictions, portfolio management, real-time data
- **Description**: Intelligent trading platform with machine learning algorithms

### 💰 **ExpenseEase – Personal Finance Tracker**
- **Technologies**: Python, Flask, SQLite, Chart.js
- **Features**: Expense tracking, budget management, financial reports
- **Description**: Simple and effective personal finance management tool

## 🛠️ **Technical Skills**

- **Programming Languages**: Python, JavaScript, Java, C++
- **Web Development**: HTML, CSS, Flask, Django
- **Databases**: PostgreSQL, MySQL, SQLite
- **Tools & Technologies**: Git, Docker, AWS, Linux

## 🎓 **Education**

- **Bachelor's Degree**: Computer Science
- **Skills Learned**: Software development, algorithms, data structures
- **Relevant Coursework**: Web development, database systems, software engineering

## 🏆 **Certifications**

- **Python Programming**: Advanced Python development skills
- **Web Development**: Full-stack web development expertise
- **Database Management**: SQL and database design proficiency

## 🔧 **Development**

### Running in Development Mode

```bash
cd backen
python3 backend.py
```

The application will run on `http://localhost:5004/` with debug mode enabled.

### Adding New Pages

1. Create HTML file in `frontend/`
2. Create CSS file in `frontend/style/`
3. Add route in `backen/backend.py`
4. Update navigation links

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

## 🤝 **Contributing**

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 **Contact**

- **Name**: [Your Name]
- **Email**: [your.email@example.com]
- **LinkedIn**: [Your LinkedIn Profile]
- **GitHub**: [Your GitHub Profile]

---

⭐ **Star this repository if you found it helpful!**

## 🚀 **GitHub Pages Setup**

To deploy this portfolio on GitHub Pages:

1. **Enable GitHub Pages** in repository settings
2. **Select source**: Deploy from a branch
3. **Choose branch**: main
4. **Select folder**: / (root)
5. **Your site will be live at**: `https://heisenberg2005-glich.github.io/Personal-Portfolio/`

**Note**: For GitHub Pages, you'll need to create static HTML versions of your pages (without Flask routes).
