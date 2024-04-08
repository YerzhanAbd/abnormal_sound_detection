import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score


model = tf.keras.models.load_model('model.h5')

testing_data = np.load('testing_x.npy')
testing_label = np.load('testing_y.npy')
predictions = model.predict(testing_data)
predicted_label = np.argmax(predictions, axis=-1) + 1
# print(np.sum(testing_label[:, 0]))
print(predicted_label)
# roc_curve(predictions, predicted_label)

metric = tf.keras.metrics.Accuracy()
metric.update_state(testing_label[:, 0],predicted_label)
print(metric.result().numpy())
import seaborn as sns

data = np.zeros((3, 3))
for index, i in enumerate(testing_label[:, 0]):
    print(i-1, predicted_label[index]-1)
    data[i-1][predicted_label[index]-1] += 1

print(data)
target_names = ['dog_bark', 'emergency', 'noise']
print(classification_report(testing_label[:, 0], predicted_label, target_names=target_names))

# fig, axs = plt.subplots(ncols=2, sharey=True, figsize=(18, 6), dpi=300)
# result = confusion_matrix(testing_label[:, 0], predicted_label, labels=target_names)
# print(result)
sns.heatmap(data, annot=True, fmt='g', cmap="crest")

# print(roc_auc_score(testing_label[:, 0], predicted_label, multi_class='ovr'))
# sns.heatmap(result, annot=True, fmt='g', cmap="crest")
plt.savefig('confusion_mat.png')