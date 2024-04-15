import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# Define the CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Load data using ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'C:/Users/PALLAVI/Desktop/new_project/Plant_Recoo/Segmented Medicinal Leaf Images',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# Train the model
model.fit_generator(
    train_generator,
    steps_per_epoch=2000,
    epochs=5)

# Function to predict plant from live camera input
def predict_plant(image):
    resized_image = cv2.resize(image, (64, 64))
    resized_image = np.expand_dims(resized_image, axis=0)
    prediction = model.predict(resized_image)
    if prediction[0][0] > 0.5:
        return "Medicinal Plant"
    else:
        return "Non-Medicinal Plant"

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Perform plant prediction
    prediction = predict_plant(frame)
    
    # Display prediction on frame
    cv2.putText(frame, prediction, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Plant Recognition', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
