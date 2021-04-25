class buatdecode:
    def decodex(kalimat):
        abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        kalimat = kalimat.lower()
        hasil_decodex = ''
        for karakter in kalimat:
            if karakter in abjad:
              nomor_lama = abjad.index(karakter)
              nomor_baru = (nomor_lama -4 ) % len(abjad)
              abjad_baru = abjad[nomor_baru]
              hasil_decodex = hasil_decodex + abjad_baru 
            else:
               hasil_decodex = hasil_decodex + ' ' 
        return hasil_decodex

