from app import app


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)


# run using using Gunicorn
# gunicorn -w 4 -b 0.0.0.0:8080 run:app
