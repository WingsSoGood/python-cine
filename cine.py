"""
mostly autogenerated:
http://starship.python.net/crew/theller/ctypes/old/codegen.html
"""

from ctypes import *


uint8_t = c_uint8
int16_t = c_int16
uint16_t = c_uint16
int32_t = c_int32
uint32_t = c_uint32
int64_t = c_int64
uint64_t = c_uint64
bool32_t = c_int
FRACTIONS = uint32_t
PFRACTIONS = POINTER(uint32_t)


class tagTIME64(Structure):
    pass
tagTIME64._fields_ = [
    ('fractions', FRACTIONS),
    ('seconds', uint32_t),
]
TIME64 = tagTIME64
PTIME64 = POINTER(tagTIME64)


class tagTC(Structure):
    pass
tagTC._fields_ = [
    ('framesU', uint8_t, 4),
    ('framesT', uint8_t, 2),
    ('dropFrameFlag', uint8_t, 1),
    ('colorFrameFlag', uint8_t, 1),
    ('secondsU', uint8_t, 4),
    ('secondsT', uint8_t, 3),
    ('flag1', uint8_t, 1),
    ('minutesU', uint8_t, 4),
    ('minutesT', uint8_t, 3),
    ('flag2', uint8_t, 1),
    ('hoursU', uint8_t, 4),
    ('hoursT', uint8_t, 2),
    ('flag3', uint8_t, 1),
    ('flag4', uint8_t, 1),
    ('userBitData', uint32_t),
]
PTC = POINTER(tagTC)
TC = tagTC


class tagTCU(Structure):
    pass
tagTCU._fields_ = [
    ('frames', uint32_t),
    ('seconds', uint32_t),
    ('minutes', uint32_t),
    ('hours', uint32_t),
    ('dropFrameFlag', bool32_t),
    ('colorFrameFlag', bool32_t),
    ('flag1', bool32_t),
    ('flag2', bool32_t),
    ('flag3', bool32_t),
    ('flag4', bool32_t),
    ('userBitData', uint32_t),
]
PTCU = POINTER(tagTCU)
TCU = tagTCU


class tagWBGAIN(Structure):
    pass
tagWBGAIN._fields_ = [
    ('R', c_float),
    ('B', c_float),
]
PWBGAIN = POINTER(tagWBGAIN)
WBGAIN = tagWBGAIN


class tagRECT(Structure):
    pass
tagRECT._fields_ = [
    ('left', int32_t),
    ('top', int32_t),
    ('right', int32_t),
    ('bottom', int32_t),
]
RECT = tagRECT
PRECT = POINTER(tagRECT)


class tagIMFILTER(Structure):
    pass
tagIMFILTER._fields_ = [
    ('dim', int32_t),
    ('shifts', int32_t),
    ('bias', int32_t),
    ('Coef', int32_t * 25),
]
PIMFILTER = POINTER(tagIMFILTER)
IMFILTER = tagIMFILTER


class tagSETUP(Structure):
    pass
tagSETUP._pack_ = 1
tagSETUP._fields_ = [
    ('FrameRate16', uint16_t),
    ('Shutter16', uint16_t),
    ('PostTrigger16', uint16_t),
    ('FrameDelay16', uint16_t),
    ('AspectRatio', uint16_t),
    ('Res7', uint16_t),
    ('Res8', uint16_t),
    ('Res9', uint8_t),
    ('Res10', uint8_t),
    ('Res11', uint8_t),
    ('TrigFrame', uint8_t),
    ('Res12', uint8_t),
    ('DescriptionOld', c_char * 121),
    ('Mark', uint16_t),
    ('Length', uint16_t),
    ('Res13', uint16_t),
    ('SigOption', uint16_t),
    ('BinChannels', int16_t),
    ('SamplesPerImage', uint8_t),
    ('BinName', c_char * 11 * 8),
    ('AnaOption', uint16_t),
    ('AnaChannels', int16_t),
    ('Res6', uint8_t),
    ('AnaBoard', uint8_t),
    ('ChOption', int16_t * 8),
    ('AnaGain', c_float * 8),
    ('AnaUnit', c_char * 6 * 8),
    ('AnaName', c_char * 11 * 8),
    ('lFirstImage', int32_t),
    ('dwImageCount', uint32_t),
    ('nQFactor', int16_t),
    ('wCineFileType', uint16_t),
    ('szCinePath', c_char * 65 * 4),
    ('Res14', uint16_t),
    ('Res15', uint8_t),
    ('Res16', uint8_t),
    ('Res17', uint16_t),
    ('Res18', c_double),
    ('Res19', c_double),
    ('Res20', uint16_t),
    ('Res1', int32_t),
    ('Res2', int32_t),
    ('Res3', int32_t),
    ('ImWidth', uint16_t),
    ('ImHeight', uint16_t),
    ('EDRShutter16', uint16_t),
    ('Serial', uint32_t),
    ('Saturation', int32_t),
    ('Res5', uint8_t),
    ('AutoExposure', uint32_t),
    ('bFlipH', bool32_t),
    ('bFlipV', bool32_t),
    ('Grid', uint32_t),
    ('FrameRate', uint32_t),
    ('Shutter', uint32_t),
    ('EDRShutter', uint32_t),
    ('PostTrigger', uint32_t),
    ('FrameDelay', uint32_t),
    ('bEnableColor', bool32_t),
    ('CameraVersion', uint32_t),
    ('FirmwareVersion', uint32_t),
    ('SoftwareVersion', uint32_t),
    ('RecordingTimeZone', int32_t),
    ('CFA', uint32_t),
    ('Bright', int32_t),
    ('Contrast', int32_t),
    ('Gamma', int32_t),
    ('Res21', uint32_t),
    ('AutoExpLevel', uint32_t),
    ('AutoExpSpeed', uint32_t),
    ('AutoExpRect', RECT),
    ('WBGain', WBGAIN * 4),
    ('Rotate', int32_t),
    ('WBView', WBGAIN),
    ('RealBPP', uint32_t),
    ('Conv8Min', uint32_t),
    ('Conv8Max', uint32_t),
    ('FilterCode', int32_t),
    ('FilterParam', int32_t),
    ('UF', IMFILTER),
    ('BlackCalSVer', uint32_t),
    ('WhiteCalSVer', uint32_t),
    ('GrayCalSVer', uint32_t),
    ('bStampTime', bool32_t),
    ('SoundDest', uint32_t),
    ('FRPSteps', uint32_t),
    ('FRPImgNr', int32_t * 16),
    ('FRPRate', uint32_t * 16),
    ('FRPExp', uint32_t * 16),
    ('MCCnt', int32_t),
    ('MCPercent', c_float * 64),
    ('CICalib', uint32_t),
    ('CalibWidth', uint32_t),
    ('CalibHeight', uint32_t),
    ('CalibRate', uint32_t),
    ('CalibExp', uint32_t),
    ('CalibEDR', uint32_t),
    ('CalibTemp', uint32_t),
    ('HeadSerial', uint32_t * 4),
    ('RangeCode', uint32_t),
    ('RangeSize', uint32_t),
    ('Decimation', uint32_t),
    ('MasterSerial', uint32_t),
    ('Sensor', uint32_t),
    ('ShutterNs', uint32_t),
    ('EDRShutterNs', uint32_t),
    ('FrameDelayNs', uint32_t),
    ('ImPosXAcq', uint32_t),
    ('ImPosYAcq', uint32_t),
    ('ImWidthAcq', uint32_t),
    ('ImHeightAcq', uint32_t),
    ('Description', c_char * 4096),
    ('RisingEdge', bool32_t),
    ('FilterTime', uint32_t),
    ('LongReady', bool32_t),
    ('ShutterOff', bool32_t),
    ('Res4', uint8_t * 16),
    ('bMetaWB', bool32_t),
    ('Hue', int32_t),
    ('BlackLevel', int32_t),
    ('WhiteLevel', int32_t),
    ('LensDescription', c_char * 256),
    ('LensAperture', c_float),
    ('LensFocusDistance', c_float),
    ('LensFocalLength', c_float),
    ('fOffset', c_float),
    ('fGain', c_float),
    ('fSaturation', c_float),
    ('fHue', c_float),
    ('fGamma', c_float),
    ('fGammaR', c_float),
    ('fGammaB', c_float),
    ('fFlare', c_float),
    ('fPedestalR', c_float),
    ('fPedestalG', c_float),
    ('fPedestalB', c_float),
    ('fChroma', c_float),
    ('ToneLabel', c_char * 256),
    ('TonePoints', int32_t),
    ('fTone', c_float * 64),
    ('UserMatrixLabel', c_char * 256),
    ('EnableMatrices', bool32_t),
    ('cmUser', c_float * 9),
    ('EnableCrop', bool32_t),
    ('CropRect', RECT),
    ('EnableResample', bool32_t),
    ('ResampleWidth', uint32_t),
    ('ResampleHeight', uint32_t),
    ('fGain16_8', c_float),
    ('FRPShape', uint32_t * 16),
    ('TrigTC', TC),
    ('fPbRate', c_float),
    ('fTcRate', c_float),
    ('CineName', c_char * 256),
    ('fGainR', c_float),
    ('fGainG', c_float),
    ('fGainB', c_float),
    ('cmCalib', c_float * 9),
    ('fWBTemp', c_float),
    ('fWBCc', c_float),
    ('CalibrationInfo', c_char * 1024),
    ('OpticalFilter', c_char * 1024),
    ('GpsInfo', c_char * 1024),
    ('Uuid', c_char * 1024),
    ('CreatedBy', c_char * 1024),
    ('RecBPP', uint32_t),
    ('LowestFormatBPP', uint16_t),
    ('LowestFormatQ', uint16_t),
    ('fToe', c_float),
    ('LogMode', uint32_t),
]
SETUP = tagSETUP
PSETUP = POINTER(tagSETUP)


class tagCINEFILEHEADER(Structure):
    pass
tagCINEFILEHEADER._fields_ = [
    ('Type', uint16_t),
    ('Headersize', uint16_t),
    ('Compression', uint16_t),
    ('Version', uint16_t),
    ('FirstMovieImage', int32_t),
    ('TotalImageCount', uint32_t),
    ('FirstImageNo', int32_t),
    ('ImageCount', uint32_t),
    ('OffImageHeader', uint32_t),
    ('OffSetup', uint32_t),
    ('OffImageOffsets', uint32_t),
    ('TriggerTime', TIME64),
]
CINEFILEHEADER = tagCINEFILEHEADER


class tagBITMAPINFOHEADER(Structure):
    pass
tagBITMAPINFOHEADER._fields_ = [
    ('biSize', uint32_t),
    ('biWidth', int32_t),
    ('biHeight', int32_t),
    ('biPlanes', uint16_t),
    ('biBitCount', uint16_t),
    ('biCompression', uint32_t),
    ('biSizeImage', uint32_t),
    ('biXPelsPerMeter', int32_t),
    ('biYPelsPerMeter', int32_t),
    ('biClrUsed', uint32_t),
    ('biClrImportant', uint32_t),
]
BITMAPINFOHEADER = tagBITMAPINFOHEADER
__all__ = ['BITMAPINFOHEADER', 'IMFILTER', 'int32_t', 'WBGAIN',
           'CINEFILEHEADER', 'int16_t', 'bool32_t', 'int64_t', 'PTCU',
           'RECT', 'tagCINEFILEHEADER', 'tagTIME64', 'uint8_t', 'TCU',
           'PTC', 'tagRECT', 'PFRACTIONS', 'PSETUP', 'TC',
           'tagIMFILTER', 'SETUP', 'tagBITMAPINFOHEADER', 'tagTCU',
           'FRACTIONS', 'tagTC', 'PIMFILTER', 'PTIME64', 'PRECT',
           'tagWBGAIN', 'uint32_t', 'tagSETUP', 'uint64_t',
           'uint16_t', 'PWBGAIN', 'TIME64']
