class UniformCheck:
    def __init__():
        pass
    
    def getMaskedContours(self, img=None, hsv_img=None, kmeans=None, morph=None, kind=None, sort=False):
        lower, upper = self.filter[kind]['lower'], self.uniform_filter[kind]['upper']
        mask = cv2.inRange(hsv_img, lower, upper)

        if kmeans:
            img_s = classification2(img, 10)
            img = classification2(img, 10)

        if morph == 'erode':
            org_mask = mask.copy()

            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 2))
            mask = cv2.erode(org_mask, k, iterations=2)

            plt_imshow(['org_mask', 'maskk', 'm2'], [org_mask, mask])

        masked_img = cv2.bitwise_and(img, img, mask=mask)

        if sort:
            contours, hierarchy = cv2.findContours(
                mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            sorted_contours, sorted_hierarchy = sortContoursByArea(
                contours, hierarchy)
            return sorted_contours, sorted_hierarchy, mask
        else:
            contours, _ = cv2.findContours(
                mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            return contours, masked_img