# CityMenderSA Django Wireframe

This repository contains a basic Django wireframe for a community issue-reporting system. It was designed to satisfy the assignment requirement for two apps, two templates, two views, and working URL routing.

## Project Structure

- `citymender/` contains the project settings and root URL configuration.
- `dashboard/` is the first app and serves the home dashboard view.
- `reports/` is the second app and serves the report issue form view.
- `templates/dashboard/home.html` is the dashboard template.
- `templates/reports/report_form.html` is the report submission template.

## Navigation and Layout

The layout uses a shared `base.html` template with a top navigation bar. From the dashboard, the user can move directly to the report form using the `Report New Issue` call-to-action or the navigation menu. The dashboard acts as the main landing page and shows quick-access buttons, report-status cards, and a recent reports list. The report form page keeps the flow simple by showing a back link, a visible progress step, an issue category field, photo upload, and location entry. This supports learnability and visibility of system status, which are both important HCI principles for this municipal reporting scenario.

## URLs

- Home dashboard: `/`
- New report form: `/reports/new/`

## GitHub Link

Replace this placeholder after you push the project:

[https://github.com/your-username/citymendersa-django-wireframe](https://github.com/your-username/citymendersa-django-wireframe)

## Screenshots

### 1. Dashboard View

![Dashboard screenshot](static/screenshots/dashboard-view.svg)

### 2. Report Form View

![Report form screenshot](static/screenshots/report-form-view.svg)

### 3. Mobile Flow Overview

![Mobile flow screenshot](static/screenshots/mobile-flow-view.svg)

## Run Instructions

1. Install Django:
   `pip install django`
2. Start the server:
   `python manage.py runserver`
3. Open:
   `http://127.0.0.1:8000/`
