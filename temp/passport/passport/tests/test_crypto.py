"""Tests the crypto interface module"""
import passport.crypto_interface as crypto
import unittest


class CryptoTest(unittest.TestCase):
    """Contains tests for the crypto interface module"""
    #key, salt, plain, encrypted
    cipher_tests = (("2b7e151628aed2a6abf7158809cf4f3c",
                     "000102030405060708090A0B0C0D0E0F", "6bc1bee22e409f96e93d7e117393172a",
                     "7649ABAC8119B246CEE98E9B12E9197D8964E0B149C10B7B682E6E39AAEB731C"),
                    ("2b7e151628aed2a6abf7158809cf4f3c",
                     "7649ABAC8119B246CEE98E9B12E9197D", "ae2d8a571e03ac9c9eb76fac45af8e51",
                     "5086CB9B507219EE95DB113A917678B255E21D7100B988FFEC32FEEAFAF23538"),
                    ("2b7e151628aed2a6abf7158809cf4f3c",
                     "5086CB9B507219EE95DB113A917678B2", "30c81c46a35ce411e5fbc1191a0a52ef",
                     "73BED6B8E3C1743B7116E69E22229516F6ECCDA327BF8E5EC43718B0039ADCEB"),
                    ("2b7e151628aed2a6abf7158809cf4f3c",
                     "73BED6B8E3C1743B7116E69E22229516", "f69f2445df4f9b17ad2b417be66c3710",
                     "3FF1CAA1681FAC09120ECA307586E1A78CB82807230E1321D3FAE00D18CC2012"),
                    ("8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b",
                     "000102030405060708090A0B0C0D0E0F", "6bc1bee22e409f96e93d7e117393172a",
                     "4F021DB243BC633D7178183A9FA071E8A647F1643B94812A175A13C8FA2014B2"),
                    ("8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b",
                     "4F021DB243BC633D7178183A9FA071E8", "ae2d8a571e03ac9c9eb76fac45af8e51",
                     "B4D9ADA9AD7DEDF4E5E738763F69145AC81CA99C3A1E883FA8D834316A2275EC"),
                    ("8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b",
                     "B4D9ADA9AD7DEDF4E5E738763F69145A", "30c81c46a35ce411e5fbc1191a0a52ef",
                     "571B242012FB7AE07FA9BAAC3DF102E0C54FCBC6DB7424CB268F588F83292023"),
                    ("8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b",
                     "571B242012FB7AE07FA9BAAC3DF102E0", "f69f2445df4f9b17ad2b417be66c3710",
                     "08B0E27988598881D920A9E64F5615CD612CCD79224B350935D45DD6A98F8176"),
                    ("603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4",
                     "000102030405060708090A0B0C0D0E0F", "6bc1bee22e409f96e93d7e117393172a",
                     "F58C4C04D6E5F1BA779EABFB5F7BFBD6485A5C81519CF378FA36D42B8547EDC0"),
                    ("603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4",
                     "F58C4C04D6E5F1BA779EABFB5F7BFBD6", "ae2d8a571e03ac9c9eb76fac45af8e51",
                     "9CFC4E967EDB808D679F777BC6702C7D3A3AA5E0213DB1A9901F9036CF5102D2"),
                    ("603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4",
                     "9CFC4E967EDB808D679F777BC6702C7D", "30c81c46a35ce411e5fbc1191a0a52ef",
                     "39F23369A9D9BACFA530E263042314612F8DA707643C90A6F732B3DE1D3F5CEE"),
                    ("603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4",
                     "39F23369A9D9BACFA530E26304231461", "f69f2445df4f9b17ad2b417be66c3710",
                     "B2EB05E2C39BE9FCDA6C19078C6A9D1B3F461796D6B0D6B2E0C2A72B4D80E644"))

    #key, salt, iterations, length, hash
    hash_tests = (("passDATA", "saltKEYbc", 16777216, 7, "AB96C76400D08B"),
                  ("password", "salt", 1, 64,
                   "867f70cf1ade02cff3752599a3a53dc4af34c7a669815ae5d513554e1c8cf252c02d470a285a0"\
                   "501bad999bfe943c08f050235d7d68b1da55e63f73b60a57fce"),
                  ("password", "salt", 2, 64,
                   "e1d9c16aa681708a45f5c7c4e215ceb66e011a2e9f0040713f18aefdb866d53cf76cab2868a39"\
                   "b9f7840edce4fef5a82be67335c77a6068e04112754f27ccf4e"),
                  ("password", "salt", 4096, 64,
                   "d197b1b33db0143e018b12f3d1d1479e6cdebdcc97c5c0f87f6902e072f457b5143f30602641b"\
                   "3d55cd335988cb36b84376060ecd532e039b742a239434af2d5"),
                  ("passwordPASSWORDpassword", "saltSALTsaltSALTsaltSALTsaltSALTsalt", 4096, 64,
                   "8c0511f4c6e597c6ac6315d8f0362e225f3c501495ba23b868c005174dc4ee71115b59f9e60cd"\
                   "9532fa33e0f75aefe30225c583a186cd82bd4daea9724a3d3b8"),

                  ("passDATAb00AB7YxDTT", "saltKEYbcTcXHCBxtjD", 100000, 63,
                   "ACCDCD8798AE5CD85804739015EF2A11E32591B7B7D16F76819B30B0D49D80E1ABEA6C9822B80"\
                   "A1FDFE421E26F5603ECA8A47A64C9A004FB5AF8229F762FF4"),
                  ("passDATAb00AB7YxDTT", "saltKEYbcTcXHCBxtjD", 100000, 65,
                   "ACCDCD8798AE5CD85804739015EF2A11E32591B7B7D16F76819B30B0D49D80E1ABEA6C9822B80A"\
                   "1FDFE421E26F5603ECA8A47A64C9A004FB5AF8229F762FF41F7C"),

                  ("passDATAb00AB7YxDTTlR", "saltKEYbcTcXHCBxtjD2P", 100000, 63,
                   "94FFC2B1A390B7B8A9E6A44922C330DB2B193ADCF082EECD06057197F35931A9D0EC0EE5C6607"\
                   "44B50B61F23119B847E658D179A914807F4B8AB8EB9505AF0"),
                  ("passDATAb00AB7YxDTTlR", "saltKEYbcTcXHCBxtjD2P", 100000, 65,
                   "94FFC2B1A390B7B8A9E6A44922C330DB2B193ADCF082EECD06057197F35931A9D0EC0EE5C6607"\
                   "44B50B61F23119B847E658D179A914807F4B8AB8EB9505AF06526"),

                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE5",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJe", 100000, 63,
                   "07447401C85766E4AED583DE2E6BF5A675EABE4F3618281C95616F4FC1FDFE6ECBC1C3982789D"\
                   "4FD941D6584EF534A78BD37AE02555D9455E8F089FDB4DFB6"),
                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE5",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJe", 100000, 65,
                   "07447401C85766E4AED583DE2E6BF5A675EABE4F3618281C95616F4FC1FDFE6ECBC1C3982789D"\
                   "4FD941D6584EF534A78BD37AE02555D9455E8F089FDB4DFB6BB30"),

                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE57U",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJemk", 100000, 63,
                   "056BC9072A356B7D4DA60DD66F5968C2CAA375C0220EDA6B47EF8E8D105ED68B44185FE9003FBB"\
                   "A49E2C84240C9E8FD3F5B2F4F6512FD936450253DB37D100"),
                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE57U",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJemk", 100000, 65,
                   "056BC9072A356B7D4DA60DD66F5968C2CAA375C0220EDA6B47EF8E8D105ED68B44185FE9003FB"\
                   "BA49E2C84240C9E8FD3F5B2F4F6512FD936450253DB37D1002889"),

                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE57Un4u12D2YD7oOP"\
                   "piEvCDYvntXEe4NNPLCnGGeJArbYDEu6xDoCfWH6kbuV6awi0",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJemkURWoqHusIeVB8"\
                   "Il91NjiCGQacPUu9qTFaShLbKG0Yj4RCMV56WPj7E14EMpbxy", 100000, 63,
                   "70CF39F14C4CAF3C81FA288FB46C1DB52D19F72722F7BC84F040676D3371C89C11C50F69BCFBC3"\
                   "ACB0AB9E92E4EF622727A916219554B2FA121BEDDA97FF33"),
                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE57Un4u12D2YD7oOP"\
                   "piEvCDYvntXEe4NNPLCnGGeJArbYDEu6xDoCfWH6kbuV6awi04",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJemkURWoqHusIeVB8"\
                   "Il91NjiCGQacPUu9qTFaShLbKG0Yj4RCMV56WPj7E14EMpbxy6", 100000, 64,
                   "2668B71B3CA56136B5E87F30E098F6B4371CB5ED95537C7A073DAC30A2D5BE52756ADF5BB2F432"\
                   "0CB11C4E16B24965A9C790DEF0CBC62906920B4F2EB84D1D4A"),
                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE57Un4u12D2YD7oOP"\
                   "piEvCDYvntXEe4NNPLCnGGeJArbYDEu6xDoCfWH6kbuV6awi04U",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJemkURWoqHusIeVB8"\
                   "Il91NjiCGQacPUu9qTFaShLbKG0Yj4RCMV56WPj7E14EMpbxy6P", 100000, 65,
                   "2575B485AFDF37C260B8F3386D33A60ED929993C9D48AC516EC66B87E06BE54ADE7E7C8CB3417C"\
                   "81603B080A8EEFC56072811129737CED96236B9364E22CE3A542"),

                  ("passDATAb00AB7YxDTTlRH2dqxDx19GDxDV1zFMz7E6QVqKIzwOtMnlxQLttpE57Un4u12D2YD7oOP"\
                   "piEvCDYvntXEe4NNPLCnGGeJArbYDEu6xDoCfWH6kbuV6awi04Uz3ebEAhzZ4ve1A2wg5CnLXdZC5Y"\
                   "7gwfVgbEgZSTmoYQSzC5OW4dfrjqiwApTACO6xoOL1AjWj6X6f6qFfF8TVmOzU9RhOd1N4QtzWI4fP"\
                   "6FYttNz5FuLdtYVXWVXH2Tf7I9fieMeWCHTMkM4VcmQyQHpbcP8MEb5f1g6Ckg5xk3HQr3wMBvQcOH"\
                   "pCPy1K8HCM7a5wkPDhgVA0BVmwNpsRIbDQZRtHK6dT6bGyalp6gbFZBuBHwD86gTzkrFY7HkOVrgc0"\
                   "gJcGJZe65Ce8v4Jn5OzkuVsiU8efm2Pw2RnbpWSAr7SkVdCwXK2XSJDQ5fZ4HBEz9VTFYrG23ELuLj"\
                   "vx5njOLNgDAJuf5JB2tn4nMjjcnl1e8qcYVwZqFzEv2zhLyDWMkV4tzl4asLnvyAxTBkxPRZj2pRAB"\
                   "Wwb3kEofpsHYxMTAn38YSpZreoXipZWBnu6HDURaruXaIPYFPYHl9Ls9wsuD7rzaGfbOyfVgLIGK5r"\
                   "ODphwRA7lm88bGKY8b7tWOtepyEvaLxMI7GZF5ScwpZTYeEDNUKPzvM2Im9zehIaznpguNdNXNMLWn"\
                   "wPu4H6zEvajkw3G3ucSiXKmh6XNe3hkdSANm3vnxzRXm4fcuzAx68IElXE2bkGFElluDLo6EsUDWZ4"\
                   "JIWBVaDwYdJx8uCXbQdoifzCs5kuuClaDaDqIhb5hJ2WR8mxiueFsS0aDGdIYmye5svmNmzQxFmdOk"\
                   "HoF7CfwuU1yy4uEEt9vPSP2wFp1dyaMvJW68vtB4kddLmI6gIgVVcT6ZX1Qm6WsusPrdisPLB2Scod"\
                   "XojCbL3DLj6PKG8QDVMWTrL1TpafT2wslRledWIhsTlv2mI3C066WMcTSwKLXdEDhVvFJ6ShiLKSN7"\
                   "gnRrlE0BnAw",
                   "saltKEYbcTcXHCBxtjD2PnBh44AIQ6XUOCESOhXpEp3HrcGMwbjzQKMSaf63IJemkURWoqHusIeVB8"\
                   "Il91NjiCGQacPUu9qTFaShLbKG0Yj4RCMV56WPj7E14EMpbxy6PlBdILBOkKUB6TGTPJXh1tpdOHTG"\
                   "6KuIvcbQp9qWjaf1uxAKgiTtYRIHhxjJI2viVa6fDZ67QOouOaf2RXQhpsWaTtAVnff6PIFcvJhdPD"\
                   "FGV5nvmZWoCZQodj6yXRDHPw9PyF0iLYm9uFtEunlAAxGB5qqea4X5tZvB1OfLVwymY3a3JPjdxTdv"\
                   "HxCHbqqE0zip61JNqdmeWxGtlRBC6CGoCiHO4XxHCntQBRJDcG0zW7joTdgtTBarsQQhlLXBGMNBSN"\
                   "mmTbDf3hFtawUBCJH18IAiRMwyeQJbJ2bERsY3MVRPuYCf4Au7gN72iGh1lRktSQtEFye7pO46kMXR"\
                   "rEjHQWXInMzzy7X2StXUzHVTFF2VdOoKn0WUqFNvB6PF7qIsOlYKj57bi1Psa34s85WxMSbTkhrd7V"\
                   "HdHZkTVaWdraohXYOePdeEvIwObCGEXkETUzqM5P2yzoBOJSdjpIYaa8zzdLD3yrb1TwCZuJVxsrq0"\
                   "XXY6vErU4QntsW0972XmGNyumFNJiPm4ONKh1RLvS1kddY3nm8276S4TUuZfrRQO8QxZRNuSaZI8JR"\
                   "Zp5VojB5DktuMxAQkqoPjQ5Vtb6oXeOyY591CB1MEW1fLTCs0NrL321SaNRMqza1ETogAxpEiYwZ6p"\
                   "IgnMmSqNMRdZnCqA4gMWw1lIVATWK83OCeicNRUNOdfzS7A8vbLcmvKPtpOFvhNzwrrUdkvuKvaYJv"\
                   "iQgeR7snGetO9JLCwIlHIj52gMCNU18d32SJl7Xomtl3wIe02SMvq1i1BcaX7lXioqWGmgVqBWU3fs"\
                   "UuGwHi6RUKCCQdEOBfNo2WdpFaCflcgnn0O6jVHCqkv8cQk81AqS00rAmHGCNTwyA6Tq5TXoLlDnC8"\
                   "gAQjDUsZp0z", 100000, 64,
                   "B8674F6C0CC9F8CF1F1874534FD5AF01FC1504D76C2BC2AA0A75FE4DD5DFD1DAF60EA7C85F122B"\
                   "CEEB8772659D601231607726998EAC3F6AAB72EFF7BA349F7F"),
                  ("passDATAb00AB", "saltKEYbcTcX", 2097152, 481,
                   "C8CB4B4B498B32CDE191159866A8E86B4C9D84EF1D0A37CF7B9BDC7872EDD5F02242AA7D83172C"\
                   "778EF64C788D622ACBCD4317C4B63A2EDE184CB2A5F6B94815C395CC822D68C637ADB0E928C969"\
                   "2D32D6B66B3825CDB6AC9B57D9D15BCA72CC32773CA45350BB460F83172B75EDD418E2C39DF437"\
                   "FFFDDEF6FF5E83AFC2974E5B391303C80B73DA815E979118FB41ACC3E2019DB30C14650DC7E75D"\
                   "67A048541563A3ECA996CF15F9B3DD7C768B45613078CF772292F092CCFEC10F027669D60EDF56"\
                   "A383894F0EFD7DDC3551E1C6AA366F7EFB39981BF0BDF7894A83D051E900AF2FB81CA990F52EE6"\
                   "13A5C2D28D28683E331F50BD10B6F8AF12705E505BCA3BB0D3869246863387DD385748718B3AAA"\
                   "51BA12BB067F1ABD6B8F2E0DECDA0A6693D1331349470E78212B2B4700709BC22C86AE7ADAB9C7"\
                   "4635BC0E40A18BE604B8BE7ED1E0419258BB0C38D27264783FE2A915CD63C7CBB6C2D937803D86"\
                   "FFE9DC58132F2AF7642C782AF6A0D50AB47622A73EF16618E15B5CE8EEE9F5A1A477A02ADB5E95"\
                   "638792811013A9A8ACC9F618C4726DC26E67C1DDCE6E1E90594C94D4DE8FD8D89400AB3E813808"\
                   "9B4CD5893BD66691708D1C27FF7E69F12D1A15983352933DE1583A2127DC8B62E345C0B1CD14F9"\
                   "F7BC85FFBCEB40E80E84E8E8C0"))

    def test_encrypt(self):
        """Test encryption by using cipher tests"""
        for test in self.cipher_tests:
            key = bytes(bytearray.fromhex(test[0]))
            salt = bytes(bytearray.fromhex(test[1]))
            plain = bytes(bytearray.fromhex(test[2]))
            cipher = bytes(bytearray.fromhex(test[3]))
            encrypted = crypto.encrypt(key, plain, salt=salt)
            encrypted = encrypted[len(salt):]
            self.assertEqual(encrypted, cipher)

    def test_encrypt_wrong_key_length(self):
        """Tests that encryption fails if wrong key size given"""
        byte_char = b'a'
        key_lengths = [0, 1, 2, 5, 10, 15, 20, 23, 30, 35, 40, 50]
        plain_text = byte_char * 32
        for length in key_lengths:
            key = length * byte_char
            self.assertRaises(ValueError, crypto.encrypt, key, plain_text)

    def test_encrypt_wrong_key_type(self):
        """Tests that encryption fails if wrong key type given"""
        types = [5, 5.4, "fes", None, True]
        plain_text = b'a' * 32
        for typ in types:
            self.assertRaises(TypeError, crypto.encrypt, typ, plain_text)

    def test_encrypt_wrong_data_type(self):
        """Tests that encryption fails if wrong data type given"""
        types = [5, 5.4, "fes", None, True]
        key = b'a' * 32
        for typ in types:
            self.assertRaises(TypeError, crypto.encrypt, key, typ)

    def test_decrypt(self):
        """Test decryption by using cipher tests"""
        for test in self.cipher_tests:
            key = bytes(bytearray.fromhex(test[0]))
            salt = bytes(bytearray.fromhex(test[1]))
            plain = bytes(bytearray.fromhex(test[2]))
            cipher = bytes(bytearray.fromhex(test[3]))
            decrypted = crypto.decrypt(key, salt + cipher)
            self.assertEqual(decrypted, plain)

    def test_decrypt_wrong_key_length(self):
        """Tests that decryption fails if wrong key size given"""
        byte_char = b'a'
        key_lengths = [0, 1, 2, 5, 10, 15, 20, 23, 30, 35, 40, 50]
        encrypted = byte_char * 32
        for length in key_lengths:
            key = length * byte_char
            self.assertRaises(ValueError, crypto.decrypt, key, encrypted)

    def test_decrypt_wrong_key_type(self):
        """Tests that decryption fails if wrong key type given"""
        types = [5, 5.4, "fes", None, True]
        encrypted = b'a' * 32
        for typ in types:
            self.assertRaises(TypeError, crypto.decrypt, typ, encrypted)

    def test_decrypt_wrong_data_type(self):
        """Tests that decryption fails if wrong data type given"""
        types = [5, 5.4, "fes", None, True]
        key = b'a' * 32
        for typ in types:
            self.assertRaises(TypeError, crypto.decrypt, key, typ)

    def test_hash_generation(self):
        """Test hash generation by hash tests"""
        for test in self.hash_tests:
            key = bytes(test[0], "utf-8")
            salt = bytes(test[1], "utf-8")
            iterations = test[2]
            length = test[3]
            predefined_hash = bytes(bytearray.fromhex(test[4]))
            generated_hash = crypto.generate_hash(key, iterations, salt=salt, length=length)
            self.assertEqual(generated_hash, predefined_hash)

    def test_hash_wrong_key_type(self):
        """Tests that hash generation fails if wrong key type given"""
        types = [5, 5.4, "fes", None, True]
        for typ in types:
            self.assertRaises(TypeError, crypto.generate_hash, typ, 1000000)

