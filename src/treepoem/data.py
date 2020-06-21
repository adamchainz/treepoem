class BarcodeType:
    def __init__(self, type_code, description):
        self.type_code = type_code
        self.description = description


# All supported barcode types, extracted from barcode.ps
barcode_types = {
    "auspost": BarcodeType("auspost", "AusPost 4 State Customer Code"),
    "azteccode": BarcodeType("azteccode", "Aztec Code"),
    "azteccodecompact": BarcodeType("azteccodecompact", "Compact Aztec Code"),
    "aztecrune": BarcodeType("aztecrune", "Aztec Runes"),
    "bc412": BarcodeType("bc412", "BC412"),
    "channelcode": BarcodeType("channelcode", "Channel Code"),
    "codablockf": BarcodeType("codablockf", "Codablock F"),
    "code11": BarcodeType("code11", "Code 11"),
    "code128": BarcodeType("code128", "Code 128"),
    "code16k": BarcodeType("code16k", "Code 16K"),
    "code2of5": BarcodeType("code2of5", "Code 25"),
    "code32": BarcodeType("code32", "Italian Pharmacode"),
    "code39": BarcodeType("code39", "Code 39"),
    "code39ext": BarcodeType("code39ext", "Code 39 Extended"),
    "code49": BarcodeType("code49", "Code 49"),
    "code93": BarcodeType("code93", "Code 93"),
    "code93ext": BarcodeType("code93ext", "Code 93 Extended"),
    "codeone": BarcodeType("codeone", "Code One"),
    "coop2of5": BarcodeType("coop2of5", "COOP 2 of 5"),
    "daft": BarcodeType("daft", "Custom 4 state symbology"),
    "databarexpanded": BarcodeType("databarexpanded", "GS1 DataBar Expanded"),
    "databarexpandedcomposite": BarcodeType(
        "databarexpandedcomposite", "GS1 DataBar Expanded Composite"
    ),
    "databarexpandedstacked": BarcodeType(
        "databarexpandedstacked", "GS1 DataBar Expanded Stacked"
    ),
    "databarexpandedstackedcomposite": BarcodeType(
        "databarexpandedstackedcomposite", "GS1 DataBar Expanded Stacked Composite"
    ),
    "databarlimited": BarcodeType("databarlimited", "GS1 DataBar Limited"),
    "databarlimitedcomposite": BarcodeType(
        "databarlimitedcomposite", "GS1 DataBar Limited Composite"
    ),
    "databaromni": BarcodeType("databaromni", "GS1 DataBar Omnidirectional"),
    "databaromnicomposite": BarcodeType(
        "databaromnicomposite", "GS1 DataBar Omnidirectional Composite"
    ),
    "databarstacked": BarcodeType("databarstacked", "GS1 DataBar Stacked"),
    "databarstackedcomposite": BarcodeType(
        "databarstackedcomposite", "GS1 DataBar Stacked Composite"
    ),
    "databarstackedomni": BarcodeType(
        "databarstackedomni", "GS1 DataBar Stacked Omnidirectional"
    ),
    "databarstackedomnicomposite": BarcodeType(
        "databarstackedomnicomposite", "GS1 DataBar Stacked Omnidirectional Composite"
    ),
    "databartruncated": BarcodeType("databartruncated", "GS1 DataBar Truncated"),
    "databartruncatedcomposite": BarcodeType(
        "databartruncatedcomposite", "GS1 DataBar Truncated Composite"
    ),
    "datalogic2of5": BarcodeType("datalogic2of5", "Datalogic 2 of 5"),
    "datamatrix": BarcodeType("datamatrix", "Data Matrix"),
    "datamatrixrectangular": BarcodeType(
        "datamatrixrectangular", "Data Matrix Rectangular"
    ),
    "datamatrixrectangularextension": BarcodeType(
        "datamatrixrectangularextension", "Data Matrix Rectangular Extension"
    ),
    "dotcode": BarcodeType("dotcode", "DotCode"),
    "ean13": BarcodeType("ean13", "EAN-13"),
    "ean13composite": BarcodeType("ean13composite", "EAN-13 Composite"),
    "ean14": BarcodeType("ean14", "GS1-14"),
    "ean2": BarcodeType("ean2", "EAN-2 (2 digit addon)"),
    "ean5": BarcodeType("ean5", "EAN-5 (5 digit addon)"),
    "ean8": BarcodeType("ean8", "EAN-8"),
    "ean8composite": BarcodeType("ean8composite", "EAN-8 Composite"),
    "flattermarken": BarcodeType("flattermarken", "Flattermarken"),
    "gs1-128": BarcodeType("gs1-128", "GS1-128"),
    "gs1-128composite": BarcodeType("gs1-128composite", "GS1-128 Composite"),
    "gs1-cc": BarcodeType("gs1-cc", "GS1 Composite 2D Component"),
    "gs1datamatrix": BarcodeType("gs1datamatrix", "GS1 Data Matrix"),
    "gs1datamatrixrectangular": BarcodeType(
        "gs1datamatrixrectangular", "GS1 Data Matrix Rectangular"
    ),
    "gs1northamericancoupon": BarcodeType(
        "gs1northamericancoupon", "GS1 North American Coupon"
    ),
    "gs1qrcode": BarcodeType("gs1qrcode", "GS1 QR Code"),
    "hanxin": BarcodeType("hanxin", "Han Xin Code"),
    "hibcazteccode": BarcodeType("hibcazteccode", "HIBC Aztec Code"),
    "hibccodablockf": BarcodeType("hibccodablockf", "HIBC Codablock F"),
    "hibccode128": BarcodeType("hibccode128", "HIBC Code 128"),
    "hibccode39": BarcodeType("hibccode39", "HIBC Code 39"),
    "hibcdatamatrix": BarcodeType("hibcdatamatrix", "HIBC Data Matrix"),
    "hibcdatamatrixrectangular": BarcodeType(
        "hibcdatamatrixrectangular", "HIBC Data Matrix Rectangular"
    ),
    "hibcmicropdf417": BarcodeType("hibcmicropdf417", "HIBC MicroPDF417"),
    "hibcpdf417": BarcodeType("hibcpdf417", "HIBC PDF417"),
    "hibcqrcode": BarcodeType("hibcqrcode", "HIBC QR Code"),
    "iata2of5": BarcodeType("iata2of5", "IATA 2 of 5"),
    "identcode": BarcodeType("identcode", "Deutsche Post Identcode"),
    "industrial2of5": BarcodeType("industrial2of5", "Industrial 2 of 5"),
    "interleaved2of5": BarcodeType("interleaved2of5", "Interleaved 2 of 5 (ITF)"),
    "isbn": BarcodeType("isbn", "ISBN"),
    "ismn": BarcodeType("ismn", "ISMN"),
    "issn": BarcodeType("issn", "ISSN"),
    "itf14": BarcodeType("itf14", "ITF-14"),
    "jabcode": BarcodeType("jabcode", "JAB Code (Beta)"),
    "japanpost": BarcodeType("japanpost", "Japan Post 4 State Customer Code"),
    "kix": BarcodeType("kix", "Royal Dutch TPG Post KIX"),
    "leitcode": BarcodeType("leitcode", "Deutsche Post Leitcode"),
    "mailmark": BarcodeType("mailmark", "Royal Mail Mailmark"),
    "matrix2of5": BarcodeType("matrix2of5", "Matrix 2 of 5"),
    "maxicode": BarcodeType("maxicode", "MaxiCode"),
    "micropdf417": BarcodeType("micropdf417", "MicroPDF417"),
    "microqrcode": BarcodeType("microqrcode", "Micro QR Code"),
    "msi": BarcodeType("msi", "MSI Modified Plessey"),
    "onecode": BarcodeType("onecode", "USPS Intelligent Mail"),
    "pdf417": BarcodeType("pdf417", "PDF417"),
    "pdf417compact": BarcodeType("pdf417compact", "Compact PDF417"),
    "pharmacode": BarcodeType("pharmacode", "Pharmaceutical Binary Code"),
    "pharmacode2": BarcodeType("pharmacode2", "Two-track Pharmacode"),
    "planet": BarcodeType("planet", "USPS PLANET"),
    "plessey": BarcodeType("plessey", "Plessey UK"),
    "posicode": BarcodeType("posicode", "PosiCode"),
    "postnet": BarcodeType("postnet", "USPS POSTNET"),
    "pzn": BarcodeType("pzn", "Pharmazentralnummer (PZN)"),
    "qrcode": BarcodeType("qrcode", "QR Code"),
    "rationalizedCodabar": BarcodeType("rationalizedCodabar", "Codabar"),
    "raw": BarcodeType("raw", "Custom 1D symbology"),
    "rectangularmicroqrcode": BarcodeType(
        "rectangularmicroqrcode", "Rectangular Micro QR Code"
    ),
    "royalmail": BarcodeType("royalmail", "Royal Mail 4 State Customer Code"),
    "sscc18": BarcodeType("sscc18", "SSCC-18"),
    "symbol": BarcodeType("symbol", "Miscellaneous symbols"),
    "telepen": BarcodeType("telepen", "Telepen"),
    "telepennumeric": BarcodeType("telepennumeric", "Telepen Numeric"),
    "ultracode": BarcodeType("ultracode", "Ultracode"),
    "upca": BarcodeType("upca", "UPC-A"),
    "upcacomposite": BarcodeType("upcacomposite", "UPC-A Composite"),
    "upce": BarcodeType("upce", "UPC-E"),
    "upcecomposite": BarcodeType("upcecomposite", "UPC-E Composite"),
}
