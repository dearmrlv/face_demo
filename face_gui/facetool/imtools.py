import torch
import torchvision.transforms as transforms
from facetool.resnet import ResNet18
from facetool.src import detect_faces, show_bboxes
from PIL import Image, ImageEnhance
import numpy as np

transform_test = transforms.Compose([  # 转换图片用的格式
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = ResNet18().to(device)
net.load_state_dict(torch.load('./facetool/net_020.pth', map_location='cpu'))
net.eval()

group = ("杜宇", "卢志颖", "吕政阳", "王政博", "章耀辉")

pixel_mean = [[67.3804504695197,78.74717133620689,92.04344340106732],
              [89.77804487179488,98.04395922364672,114.16550925925925],
              [101.07728630514706,106.85868853400736,126.85310489430147],
              [93.39816273834745,102.48243842690678,116.67317597987288],
              [73.45789080501152,80.42473718317973,91.67611427131337]]

def PIL_to_tensor(image):
    image = transform_test(image).unsqueeze(0)
    return image.to(device, torch.float)

def faceclassify(img):
    # img: the facial part of the frame
    img = img.resize((32, 32))
    iImg = PIL_to_tensor(img)
    output = net(iImg)
    _, predicted = torch.max(output.data, 1)
    # print(group[predicted.data])
    return group[predicted.data]

def get_group():
    return group

def get_faces(frame):
    # frame: a frame captured by the camera
    # returns an array contains all the faces in the frame

    img = Image.fromarray(frame, mode=None)
    bounding_boxes, landmarks = detect_faces(img)
    if len(bounding_boxes) != 0 and len(landmarks) != 0:
        bounding_boxes_tmp = []
        landmarks_tmp = []
        if len(bounding_boxes) != 0:
            bounding_boxes_tmp.append(bounding_boxes[0])
        if len(landmarks) != 0:
            landmarks_tmp.append(landmarks[0])
        image_2 = show_bboxes(img, bounding_boxes_tmp, landmarks_tmp)
        frame = np.array(image_2)
        faces = []
        for b in bounding_boxes:
            region = (b[0], b[1], b[2], b[3])
            face_cut = image_2.crop(region)
            face_cut = face_cut.resize((32, 32))
            faces.append(face_cut)

    else:
        faces = []

    return faces, frame

def get_mean(face_img):
    r, g, b = face_img.split()
    ar = np.array(r).flatten()
    ag = np.array(g).flatten()
    ab = np.array(b).flatten()

    return [ar.mean(), ag.mean(), ab.mean()]

def get_label(name):
    return {
        '杜宇': 1,
        '卢志颖': 2,
        '吕政阳': 3,
        '王政博': 4,
        '章耀辉': 5,
    }.get(name, 'error')

def pixel_trans(face, name):
    face_mean = get_mean(face)
    label = get_label(name)
    tmp = np.array(face)

    # Linear transform
    try:
        for i in range(3):
            tmp[:,:,i] = tmp[:,:,i] * pixel_mean[label][i] / face_mean[i]
    except: IndexError
    return Image.fromarray(tmp)

def brighter_frame(frame, brightness):
    frame_img = Image.fromarray(frame)
    en = ImageEnhance.Brightness(frame_img)
    en_end = en.enhance(brightness)
    return np.array(en_end)

def brighter_face(face, brightness):
    en = ImageEnhance.Brightness(face)
    return en.enhance(brightness)