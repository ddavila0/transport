#include "msquic.h"
#include "client.h"
#ifndef UTILS_H
#define UTILS_H

void WriteSslKeyLogFile(const char* FileName, QUIC_TLS_SECRETS* TlsSecrets);

#endif
