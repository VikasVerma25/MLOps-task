#!/usr/bin/env python

from keras.datasets import mnist

dataset = mnist.load_data()

(X_train, y_train), (X_test, y_test) = dataset

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)        # converting to 4D
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255      # normalising the RGB codes
X_test /= 255

from keras.models import Sequential
from keras.layers import Dense, Convolution2D, Flatten, MaxPooling2D
model = Sequential()

import variables
model.add(Convolution2D(filters = variables.filter_no, kernel_size=(5,5), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Flatten()) 
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10,activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', 
             metrics=['accuracy']
             )
model.fit(X_train, y_train, epochs = variables.epoch_no)

accuracy = model.evaluate(X_test, y_test)[1]

accuracy = round(accuracy*100, 3)

print(f"accuracy {accuracy} %")

from os import system
if accuracy > 98:
    system("echo 'true' > /code/accuracy.txt")
else:
    system("echo 'false' > /code/accuracy.txt")


import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "vikasverma.new1@gmail.com"  # Enter your address
receiver_email = "vikasverma250999@gmail.com"  # Enter receiver address
password = '' # Enter password
if accuracy > 98:
    message = """\
Subject: model-prediction 

Congratulations {} % accuracy achieved.""".format(accuracy)
    
else:
    message = """\
Subject: model-prediction 

Got {} % accuracy, Training Again!""".format(accuracy)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

