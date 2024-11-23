import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical, plot_model

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from pathlib import Path
from config import (
    DATA_INPUT_PATH,
    CLASSES,
    MODEL_PATH,
    METADATA_PATH,
)

# Read all of the files in the data folder
files_in_folder = Path(DATA_INPUT_PATH).rglob("*.csv")
files = [x for x in files_in_folder]

# Read the data from the files
dfs = []

for file in files:
    df = pd.read_csv(str(file))
    dfs.append(df)
        
# Convert the data to a DataFrame
df = pd.concat([x for x in dfs], axis=0)
print(df.head())

# Before removing duplicates
print(f"Shape of dataframe before removing duplicates {df.shape}")
# Remove duplicates
df = df.drop_duplicates()
print(f"Shape of dataframe after removing duplicates {df.shape}")

X = df.drop(columns=['Label'])
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# filter for valid classes because the data is not clean
valid_classes = [0, 1, 2, 3, 4, 5, 6, 7]
mask_train = y_train.isin(valid_classes)
mask_test = y_test.isin(valid_classes)

# apply the mask to the training and testing data
X_train_filtered = X_train_scaled[mask_train]
y_train_filtered = y_train[mask_train]

X_test_filtered = X_test_scaled[mask_test]
y_test_filtered = y_test[mask_test]

# one hot encode the target data
y_train_categorical = to_categorical(y_train_filtered, num_classes=8)
y_test_categorical = to_categorical(y_test_filtered, num_classes=8)

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train_filtered.shape[1],)))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5)) 
model.add(Dense(32, activation='relu'))
model.add(Dense(8, activation='softmax'))  # Softmax for 8 output classes

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=2,
    restore_best_weights=True
)
# Compile the model with categorical crossentropy for multi-class classification
model.compile(
    optimizer=Adam(learning_rate=0.001), 
    loss='categorical_crossentropy', 
    metrics=['accuracy'],
)

# Train the model using the filtered training data
model.fit(X_train_filtered, y_train_categorical, epochs=10, batch_size=64, validation_split=0.2, callbacks=[early_stopping])

# Evaluate the model on the filtered test set
test_loss, test_acc = model.evaluate(X_test_filtered, y_test_categorical)

print(f"Test accuracy: {test_acc}")