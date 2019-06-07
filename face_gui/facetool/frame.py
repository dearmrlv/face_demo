from facetool.face import Face
from facetool.imtools import get_faces, brighter_frame

class Frame():
    def __init__(self, frame):
        self.faces, self.frame = get_faces(frame)
        self.face_num = len(self.faces)

    def name_checked(self):
        self.names = []
        for face in self.faces:
            face_checked = Face(face)
            # self.names.append(face_checked.name)
            # self.names.append(face_checked.name_affirm())
            self.names = face_checked.name_affirm()
            break   # just select the first face for detect
            # name_checked = face_checked.name
            # print("Welcome! "+name_checked)

    def re_detect(self, brightness):
        if len(self.names) == 0:
            self.frame = brighter_frame(self.frame, brightness)
            self.faces, self.frame = get_faces(self.frame)
            self.face_num = len(self.faces)
            self.name_checked()
