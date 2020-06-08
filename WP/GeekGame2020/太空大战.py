import hashlib

mask = [ 
            0xc190, 0x6794, 0x3e74, 0x7523, 0xcea6, 0x817f, 0x1f96, 0x9bf0, 0xe14, 0x53f9, 0x4d96, 0x2fec, 0xc686, 0x65ff, 0x8a3f, 0x50b5,
            0x18e2, 0x36cd, 0x6853, 0xa78a, 0x4bbf, 0x360c, 0xeeae, 0x9731, 0xb067, 0x327f, 0xbab2, 0x990f, 0x5128, 0xadf4, 0x49ed, 0x12f6,
            0xecb4, 0x2ea5, 0x7142, 0x2b9e, 0xe0f2, 0xbf16, 0x338f, 0xa416, 0xf53d, 0x7af8, 0xc520, 0xd285, 0x52f1, 0xf010, 0xda22, 0xb5ff,
            0x294e, 0xb0c5, 0xc72f, 0xaf42, 0xb379, 0x42d1, 0x6a89, 0x49ed, 0xa029, 0xfb36, 0xca86, 0xb4c7, 0x3a81, 0xee97, 0x66da, 0x4a8,
            0xef06, 0x984d, 0x8d41, 0x4269, 0x96b0, 0xc19f, 0xda79, 0x7c0f, 0xd516, 0x31d7, 0x35bc, 0xee01, 0x8e0d, 0x6aac, 0xdf2c, 0xa5f3,
            0xa517, 0xdefe, 0xda1f, 0x3500, 0x9147, 0x47d4, 0x8720, 0x105d, 0xffd4, 0x6061, 0x6988, 0x1b1d, 0x81cd, 0x1054, 0x8a7e, 0xfd6a,
            0x8f64, 0x59a4
]

secert = 'jFEQ6xFkUxKGzUbn'

for i in range(1,181):
    secert += str(mask[i % len(mask)])
    secert = hashlib.md5(secert.encode()).hexdigest()

print('scuctf{' + secert[0:16] + '}')
