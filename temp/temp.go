package main

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
)

func PKCS7Padding(ciphertext []byte, blockSize int) []byte {
	padding := blockSize - len(ciphertext)%blockSize
	padtext := bytes.Repeat([]byte{byte(padding)}, padding)
	return append(ciphertext, padtext...)
}

func PKCS7UnPadding(origData []byte) []byte {
	length := len(origData)
	unpadding := int(origData[length-1])
	return origData[:(length - unpadding)]
}

func AesEncrypt(origData, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	blockSize := block.BlockSize()
	origData = PKCS7Padding(origData, blockSize)
	blockMode := cipher.NewCBCEncrypter(block, key[:blockSize])
	crypted := make([]byte, len(origData))
	blockMode.CryptBlocks(crypted, origData)
	return crypted, nil
}

func AesDecrypt(crypted, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	blockSize := block.BlockSize()
	blockMode := cipher.NewCBCDecrypter(block, key[:blockSize])
	origData := make([]byte, len(crypted))

	blockMode.CryptBlocks(origData, crypted)
	fmt.Printf("%x\n", crypted)
	origData = PKCS7UnPadding(origData)
	return origData, nil
}

func main() {
	key := []byte("give_your_A3sk4y")
	cont, err := base64.StdEncoding.DecodeString(string("Zhku//KtcRA2RNEksxSRrwJIP3Szu/7hrQR5+JO/aTc="))
	if err != nil {
		panic(err)
	}
	result, err := AesDecrypt(cont, key)
	if err != nil {
		panic(err)
	}
	fmt.Println(base64.StdEncoding.EncodeToString(result)) //JGw3SXR8bk5xVXY8dUN7aWY1QjJkamhOQVM9fEI=，这里输出Base64模式

}
