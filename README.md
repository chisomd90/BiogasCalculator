# Biogas Calculator

This Django project provides a web application for calculating biogas production based on the characteristics of mixed wastes. It allows users to input the ratio of Food Waste Vegetables (FVW) and Cow Manure (CM) and calculates the corresponding biogas production per gram.

## Features

- Calculate biogas production based on input ratios of FVW and CM.
- Display the calculated biogas production in milliliters per gram (mL/g).
- Store waste characteristics and biogas production results in the database.

## Requirements

- Python 3.x
- Django

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chisomd90/BiogasCalculator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BiogasCalculator
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to create database tables:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://127.0.0.1:8000/calculate-biogas/` in your web browser.

## Usage

1. Input the ratio of FVW and CM in the provided form.
2. Click the "Calculate" button to calculate biogas production.
3. View the calculated biogas production in mL/g.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
