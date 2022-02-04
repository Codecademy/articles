import os
import tensorflow as tf

dataset_link = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
training_data = tf.keras.utils.get_file(fname=os.path.basename(dataset_link), origin=dataset_link)
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
features=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
label = 'species'
classes = ['setosa', 'versicolor', 'virginica']
batch_size = 32
tf_dataset = tf.data.experimental.make_csv_dataset(training_data,batch_size, column_names=columns,label_name=label,num_epochs=1)
f, l = next(iter(tf_dataset))
def helper(features, labels):
  f = tf.stack(list(features.values()), axis=1)
  return f, labels
tf_dataset = tf_dataset.map(helper)
f, l = next(iter(tf_dataset))


model = tf.keras.Sequential([tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(4,)), tf.keras.layers.Dense(10, activation=tf.nn.relu), tf.keras.layers.Dense(3)])
loss_obj = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
def loss(model, x, y, training):
  y_new = model(x, training=training)
  return loss_obj(y_true=y, y_pred=y_new)
def grad(model, inputs, targets):
  with tf.GradientTape() as g:
    loss_val = loss(model, inputs, targets, training=True)
  return loss_val, g.gradient(loss_val, model.trainable_variables)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
loss_result = []
accuracy = []
num = 201
for n in range(num):
  loss_avg = tf.keras.metrics.Mean()
  n_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
  for x, y in tf_dataset:
    loss_value, grads = grad(model, x, y)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    loss_avg.update_state(loss_value)  # Add 
    n_accuracy.update_state(y, model(x, training=True))
  loss_result.append(loss_avg.result())
  accuracy.append(n_accuracy.result())
  if n % 50 == 0:
    print("n {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(n,loss_avg.result(),n_accuracy.result()))
testset_link = "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"
test_data = tf.keras.utils.get_file(fname=os.path.basename(testset_link),origin=testset_link)
tf_testset = tf.data.experimental.make_csv_dataset(test_data,batch_size,column_names=columns,label_name='species',num_epochs=1,shuffle=False)
tf_testset = tf_testset.map(helper)
model_accuracy = tf.keras.metrics.Accuracy()
for (x, y) in tf_testset:
  logits = model(x, training=False)
  prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
  model_accuracy(prediction, y)
print("Model accuracy is {:.3%}".format(model_accuracy.result()))

