

class MagnetLink:
    def __init__(self, hash, nid='btih', xl=None, dn=None, tr=None, aas=None, xs=None, kt=None, mt=None):
        self.dn = dn # filename
        self.xl = xl # size in bytes
        self.hash = hash # file hash
        self.aas = aas # web link to the file online
        self.xs = xs # P2P link
        self.kt = kt # key words for search
        self.mt = mt # link to the metafile that contains a list of magneto
        self.tr = tr # tracker URL for BitTorrent download
        self.nid = nid  # namespace identifier
        self.magnetLink = 'magnet:?' #magnet URI


    def __call__(self):

        self.ml_constructor()
        return self.magnetLink

    def ml_constructor(self):
        self.paramDict = {self.xl : 'xl={}&'.format(self.xl),
                        self.dn : 'dn={}&'.format(self.dn),
                        self.hash : 'xt=urn:{}:{}'.format(self.nid, self.hash)}

        for param in self.paramDict.keys():
            if param:
                self.magnetLink += self.paramDict[param]



if __name__ == '__main__':

    ml = MagnetLink('c12fe1c06bca254a9dc9f519b784ba7c1367a88a', dn='Zader', nid='sha1')
    print(ml())