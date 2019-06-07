from facetool.imtools import faceclassify, get_group, pixel_trans, brighter_face

MAX_RECURSIVE = 10

class Face:
    def __init__(self,face):
        # face: the face part in a frame, a variable after function Image.open()
        # group: the group the face belongs to, a tuple contains the names in the group
        # name: the corresponding name to the face

        self.face = face    # represents only one face
        self.group = get_group()
        # self.name = faceclassify(self.face)
        # self.recursive = 0

    def name_affirm(self):
        # self.recursive += 1
        names = []
        for name in self.group:
            tmp_face = brighter_face(self.face, 2)
            # tmp_face = pixel_trans(self.face, name)
            tmp_face = pixel_trans(tmp_face, name)
            tmp_name = faceclassify(tmp_face)
            if tmp_name == name:
                names.append(tmp_name)

        return names
        # else:
        #     if self.recursive > MAX_RECURSIVE:
        #         return 'Failed'
        #     else:
        #         self.face = tmp_face
        #         self.name = tmp_name
        #         self.name_affirm(self)
