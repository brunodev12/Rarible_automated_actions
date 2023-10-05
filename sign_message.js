const sigUtil = require('eth-sig-util');
const ethUtil = require('ethereumjs-util');

function signTypedMessage(message) {

    if (message === null){
        return null;
    }

    let messageObject;

    try {
        messageObject = JSON.parse(message);
    } catch (error) {
        return null;
    }

    const privateKeyOrigin = process.env.PRIVATE_KEY;
    const privateKey = ethUtil.toBuffer('0x' + privateKeyOrigin);
    const messageHash = sigUtil.TypedDataUtils.sign(messageObject);
    const sig = ethUtil.ecsign(messageHash, privateKey);
    const serializedSig = ethUtil.bufferToHex(sigUtil.concatSig(sig.v, sig.r, sig.s));
    console.log(serializedSig);
}

signTypedMessage(process.argv[2]);

