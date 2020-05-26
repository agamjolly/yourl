# 🔗Yourl
A URL shortner written in Flask, made using a NoSQL database with internal hashing protocols taking care of possible hash collisions and dynamic routing. 

## Cloning

To clone the repository, shift to the directory where you want the source to be. This can be done using

```bash
cd <path>
```

You can clone the repository using

```bash
git clone https://www.github.com/agamjolly/yourl.git
```

## Usage

You can run the Flask backend by installing all dependencies using `pip3` and then installing a virtual environment (recommended) and then running

```bash
export FLASK_APP=app.py
```

This should compile a production build of the app, suitable for deployment. 

If you want to run the development build for testing, you can change the export settings and run

```bash
export FLASK_ENV=development
```

To finally run the Flask app, you should run

```bash
flask run
```

The app should be live on port 5000, unless specified otherwise. 

## Contributing

Feel free to contribute by forking, pulling your own branch and initiating pull/merge requests. Hit me up on email if you have any queries!
