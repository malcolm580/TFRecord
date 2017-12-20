import tensorflow as tf

if __name__ == '__main__':
    for serialized_example in tf.python_io.tf_record_iterator("train/train.record"):
        example = tf.train.Example()
        example.ParseFromString(serialized_example)

        filename = example.features.feature['image/filename'].bytes_list.value
        label = example.features.feature['image/object/class/label'].int64_list.value
        classText = example.features.feature['image/object/class/text'].bytes_list.value

        print('filename =', filename, 'label =', label, 'classText =',  classText)
