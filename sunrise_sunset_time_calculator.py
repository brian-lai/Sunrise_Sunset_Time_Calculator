# -*- coding: utf-8 -*-
# --------------------------------------------------------------------
# Sunrise_Sunset_Calculator.py
# Created on:   1/7/2016
# Created by:   Brian Lai
# Usage:        Calculates Sunrise and Sunset times
# Description:  Calculates Sunrise and Sunset times based on location
#               and determines length of time spent in darkness
# --------------------------------------------------------------------



########    Equation Set for Calculating Sunrise and Sunset Times in UTC    ########
class Sunrise_Sunset_Calculator(object):
    D_0 = 2400000.5
    MJD_JD2000 = 51544.5

    def __init__(self, latitude, longitude):
        """Initialize new Sunrise_Sunset_Calculator class object"""
        self.label = "Sunrise_Sunset_Calculator"
        self.latitude = latitude
        self.longitude = longitude





   def ipart(q):
        return modf(q)[1]

    def ReDate(Date):
        day = ipart(Date/10000)
     month = ipart((Date - (day * 10000)) / 100)
        remove = ipart(Date/100)
        yr = (Date - remove * 100)
        if yr/1000 < 1:
            year = 2000 + ipart(yr)
        else:
            year = yr
        RD = [day, month, year]

    return RD

    def gcal2jd(year, month, day):
        a = ipart((month - 14) / 12.0)
        jd = ipart((1461 * (year + 4800 + a)) / 4.0)
        jd += ipart((367 * (month - 2 - 12 * a)) / 12.0)
        x = ipart((year + 4900 + a) / 100.0)
        jd -= ipart((3 * x) / 4.0)
        jd += day - 2432075.5

        JD = MJD_0 + jd

        return JD

    def JulianCentury(JD):
        JC = ((JD - 2451545) / 36525)
        return JC

    def GeomMeanLongSun(JC):
        GMLS = (280.46646 + JC * (36000.76983 + JC * 0.0003032)) % 360
        return GMLS

    def mMeanAnomSun(JC):
        GMAS = 357.52911 + JC*(35999.05029 - JC*(0.0001537))
        return GMAS

    def EccrthOrbit(JC):
        EEO = 0.016708634 - JC * (0.000042037 + 0.0000001267 * JC)
        return EEO

    def SunEqofCtr(GMAS, JC):
        SEoC = sin(radians(GMAS)) * (1.914602 - JC * (0.004817 + 0.000014 * JC)) + sin(radians(2 * GMAS)) * (0.019993 - 0.000101 * JC) + sin(radians(3 * GMAS)) * 0.000289
        return SEoC

    def SunTrueLong(GMLS, SEoC):
        STLong = (GMLS + SEoC)
        return STLong

    def SunRadVector(EEO, STAnom):
        SRVector = (1.000001018 * (1-EEO*EEO)) / (1 + EEO * cos(radians(STAnom)))
        return SRVctor

    def SunAppLong(STLong, JC):
        SAL = STLong - 0.00569 - 0.00478 * sin(radians(125.04 - 1934.136 * JC))
        return SAL

    def MeanObliqEcliptic(JC):
        MOE = 23 + (26 + ((21.448 - JC*(46.815 + JC*(0.00059 - JC*(0.001813)))))/60)/60
        return MOE

    def ObliqCorr(MOE, JC):
        OC = MOE + 0.00256 * cos(radians(125.04 - 1934.136*(JC)))
        return OC

    def SunRtAscen(SAL, OC):
        SRA = degrees(atan2(cos(radians (SAL)),cos(radians(OC))*sin(radians(SAL))))
        return SRA

    def SunDeclin(SAL, OC):
        SDecline = degrees(asin(sin(radians(OC)) * sin(radians(SAL))))
        return SDece

    def varY(OC):
        vY = tan(radians(OC / 2)) * tan(radians(OC / 2))
        return vY

    def EqofTime(vY, GMLS, EEO, GMAS):
        EoT = 4 * degrees(vY * sin(2 * radians(GMLS)) - 2 * EEO * sin(radians(GMAS)) + 4 * EEO * vY * sin(radians(GMAS)) * cos(2 * radians(GMLS)) - 0.5 * vY * vY * sin(4 * radians(GMLS)) - 1.25 * EEO * EEO * sin(2 * radians(GMAS)))
        return EoT

    def HASunrise(SDecline, Lat):
        HASun = degrees(acos(cos(radians(90.833))/(cos(radians(Lat))*cos(radians(SDecline)))-tan(radians(Lat))*tan(radians(SDecline))))
        return HASun

    def SolarNoon(EoT, Lon, TimeZone):
        SNoon = (720 - 4 * float(Lon) - float(EoT) + float(TimeZone) * 60) / 1440
        return SNoon

    def SunriseTime(SNoon,HASun):
        SriseTime = (SNoon * 1440 - HASun * 4) / 1440
        return SriseTime

    def SunsetTime(SNoon,HASun):
        SsetTime = (SNoon * 1440 + HASun * 4) / 1440
        return SsetTime

    def ConvertTime(:
        a = 240000 * UTC
        hr_1 = modf(a/10000)[1]
        hr_2 = (modf(a/10000)[0] * 100)/60
        hr = 10000 * (hr_1 + modf(hr_2)[1])
        mn = (modf(((a - hr_1*10000)/100) % 60)[1] + modf(modf(a/100)[0] * 100/60)[1]) *100
        sec = (modf(a/100) %60
        Time = hr + mn + sec
      turn Time

    def main(Date,Lat,Lon,TimeZone):
        day = ReDate(Date)[0]
        month = ReDate(Date)[1]
        year = ReDate(Date)[2]
        JD = gcal2jd(year, month, day)
        JC = JulianCentury(JD)
        GMLS = GeomMeanLongSun(JC)
        GMAS = GeomMeanAnomSun(JC)
        EEO = EccentEarthOrbit(JC)
        SEoC = SunEqofCtr(GMAS, JC)
        STLong = SunTrueLong(GMLS,SEoC)
        SAL = SunAppLong(STLong,JC)
      MOE = MeanObliqEcliptic(JC)
        OC = ObliqCorr(MOE,JC)
        SDecline = SunDeclin(SAL,OC)
        vY = varY(OC)
        EoT = EqofTime(vY,GMLS,EEO,GMAS)
        HASun = HASunrise(SDecline,Lat)
        SNoon = SolarNoon(EoT,Lon,TimeZone)
        SriseTime = SunriseTime(SNoon,HASun)
        SsetTime = SunsetTime(SNoon,HASun)

        RiseSet = [SriseTime, SsetTime]

        return RiseSet
