#ifndef UTILS_H
#define UTILS_H

void WriteSslKeyLogFile(const char* FileName, QUIC_TLS_SECRETS* TlsSecrets);
void PrintUsage();
BOOLEAN GetFlag(int argc, char* argv[],const char* name);
const char* GetValue(int argc, char* argv[],const char* name);
uint8_t DecodeHexChar(char c);
uint32_t DecodeHexBuffer(const char* HexBuffer, uint32_t OutBufferLen,uint8_t* OutBuffer);
void EncodeHexBuffer(uint8_t* Buffer, uint8_t BufferLen,char* HexString);

#endif
