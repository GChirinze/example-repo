# example-repo
# 📰 Capstone News Application

A comprehensive news platform built with Django that enables independent journalists and publishers to share content with subscribers through a robust role-based system.

## 🚀 Features

### Core Functionality
- **Role-Based Access Control** (Reader, Journalist, Editor)
- **Article Management** with editorial approval workflow
- **Subscription System** for publishers and individual journalists
- **Email Notifications** for approved articles
- **RESTful API** for third-party integrations
- **X (Twitter) Integration** for social media sharing

### User Roles & Permissions
- **👥 Readers**: View articles, subscribe to publishers/journalists
- **✍️ Journalists**: Create/edit articles and newsletters
- **📋 Editors**: Review, approve, and manage content

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7, Django REST Framework
- **Database**: MariaDB/MySQL (Production), SQLite (Development)
- **Authentication**: Django Auth with Custom User Model
- **API**: RESTful API with JSON serialization

## 📋 Prerequisites

- Python
- MariaDB/MySQL database
- Virtual Environment

## ⚡ Quick Start

### 1. Clone & Setup
```bash
# Clone the project
git clone <repository-url>
cd news_app

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt