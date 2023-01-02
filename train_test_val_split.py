import os
import shutil

root = r"D:\kaggle_practice\Blood_Cell_Detection"

test_set = r"D:\kaggle_practice\Blood_Cell_Detection\Split_declaration\test.txt"
train_set = r"D:\kaggle_practice\Blood_Cell_detection\Split_declaration\train.txt"
val_set = r"D:\kaggle_practice\Blood_Cell_detection\Split_declaration\val.txt"

train_path = r"D:\kaggle_practice\Blood_Cell_Detection\train\images"
train_label = r"D:\kaggle_practice\Blood_Cell_Detection\train\labels"
test_path = r"D:\kaggle_practice\Blood_Cell_Detection\test\images"
test_label = r"D:\kaggle_practice\Blood_Cell_Detection\test\labels"
val_path = r"D:\kaggle_practice\Blood_Cell_Detection\valid\images"
val_label = r"D:\kaggle_practice\Blood_Cell_Detection\valid\labels"


def createTrainingSet():
    train_file = open(train_set, 'r')
    for line in train_file:
        # print(line.strip())
        for filename in os.listdir(os.path.join(root, "images")):
            # f = os.path.join(root, filename)
            # print(filename.rsplit('.', 1)[0])
            if filename.rsplit('.', 1)[0] == line.strip():
                # print("True")
                # print(os.path.join(root, filename))
                shutil.copy(os.path.join(os.path.join(root, "images"), filename), train_path)
                print("moved ", filename, " To training set")

        for filename in os.listdir(os.path.join(root, "labels")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "labels"), filename), train_label)


def createTestingSet():
    test_file = open(test_set, 'r')
    for line in test_file:
        # print(line.strip())
        for filename in os.listdir(os.path.join(root, "images")):
            # f = os.path.join(root, filename)
            # print(filename.rsplit('.', 1)[0])
            if filename.rsplit('.', 1)[0] == line.strip():
                # print("True")
                # print(os.path.join(root, filename))
                shutil.copy(os.path.join(os.path.join(root, "images"), filename), test_path)
                print("moved ", filename, " To testing set")
        for filename in os.listdir(os.path.join(root, "labels")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "labels"), filename), test_label)


def createValidationSet():
    val_file = open(val_set, 'r')
    for line in val_file:
        # print(line.strip())
        for filename in os.listdir(os.path.join(root, "images")):
            # f = os.path.join(root, filename)
            # print(filename.rsplit('.', 1)[0])
            if filename.rsplit('.', 1)[0] == line.strip():
                # print("True")
                # print(os.path.join(root, filename))
                shutil.copy(os.path.join(os.path.join(root, "images"), filename), val_path)
                print("moved ", filename, " To Validation set")
        for filename in os.listdir(os.path.join(root, "labels")):
            if filename.rsplit('.', 1)[0] == line.strip():
                shutil.copy(os.path.join(os.path.join(root, "labels"), filename), val_label)


createTrainingSet()

createTestingSet()

createValidationSet()
