from codecs import decode,encode
import uu

orig="M22!T:&EN:R!I=\"!D;V5S(&YO=\"!T86ME('1I;65S+\"!I=\"=S('9E<GD@<VEM M<&QE+@I!;GEW87DL(&AE<F4@:7,@=&AE(&9L86<@9F]R('EO=3H@2W5N0U1& 3>W5U9&5C;V1E<E]I<U]D;VYE?0"
encoding_types=['uu','base-64']
for et in encoding_types:
    enc_data=encode(orig.encode(),et)
    un_enc_data=decode(enc_data,et)
    print("\n\nEncoding  : {}".format(et))
    print("Orig          : {}".format(orig))
    print("Encoded       : {}".format(enc_data))
    print("byte UnEncoded: {}".format(un_enc_data))
    print("utf8 UnEncoded: {}".format(un_enc_data.decode()))