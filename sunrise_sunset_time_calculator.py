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
class SunRiseSet(object):
    D_0 = 2400000.5
    MJD_JD2000 = 51544.5

    def __init__(self, date, latitude, longitude, timezone):
        """Initialize new Sunrise_Sunset_Calculator class object"""
        self.name = "Sunrise Sunset Calculator"
        self.date = date
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        return

    def



    def ipart(q):
        return modf(q)[1]

    def redate(Date):
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

    def gregorian_calendar_to_julian_date(year, month, day):
        a = ipart((month - 14) / 12.0)
        jd = ipart((1461 * (year + 4800 + a)) / 4.0)
        jd += ipart((367 * (month - 2 - 12 * a)) / 12.0)
        x = ipart((year + 4900 + a) / 100.0)
        jd -= ipart((3 * x) / 4.0)
        jd += day - 2432075.5
        gc2jd = MJD_0 + jd
        return gc2jd

    def julian_century(JD):
        JC = ((JD - 2451545) / 36525)
        return JC

    def geometric_mean_longitude_sun(JC):
        GMLS = (280.46646 + JC * (36000.76983 + JC * 0.0003032)) % 360
        return GMLS

    def geometric_mean_anomaly_sun(JC):
        GMAS = 357.52911 + JC*(35999.05029 - JC*(0.0001537))
        return GMAS

    def eccentricity_earth_orbit(JC):
        EEO = 0.016708634 - JC * (0.000042037 + 0.0000001267 * JC)
        return EEO

    def sun_equation_of_center(GMAS, JC):
        SEoC = sin(radians(GMAS)) * (1.914602 - JC * (0.004817 + 0.000014 * JC)) + sin(radians(2 * GMAS)) * (0.019993 - 0.000101 * JC) + sin(radians(3 * GMAS)) * 0.000289
        return SEoC

    def sun_true_longitude(GMLS, SEoC):
        STLong = (GMLS + SEoC)
        return STLong

    def sun_radius_vector(EEO, STAnom):
        SRVector = (1.000001018 * (1-EEO*EEO)) / (1 + EEO * cos(radians(STAnom)))
        return SRVctor

    def sun_approximate_longitude(STLong, JC):
        SAL = STLong - 0.00569 - 0.00478 * sin(radians(125.04 - 1934.136 * JC))
        return SAL

    def mean_obliquity_of_ecliptic(JC):
        MOE = 23 + (26 + ((21.448 - JC*(46.815 + JC*(0.00059 - JC*(0.001813)))))/60)/60
        return MOE

    def obliquity_correction(MOE, JC):
        OC = MOE + 0.00256 * cos(radians(125.04 - 1934.136*(JC)))
        return OC

    def SunRtAscen(SAL, OC):
        SRA = degrees(atan2(cos(radians(SAL)),cos(radians(OC))*sin(radians(SAL))))
        return SRA

    def sun_declination(SAL, OC):
        SDecline = degrees(asin(sin(radians(OC)) * sin(radians(SAL))))
        return SDece

    def varY(OC):
        vY = tan(radians(OC / 2)) * tan(radians(OC / 2))
        return vY

    def equation_of_time(vY, GMLS, EEO, GMAS):
        EoT = 4 * degrees(vY * sin(2 * radians(GMLS)) - 2 * EEO * sin(radians(GMAS)) + 4 * EEO * vY * sin(radians(GMAS)) * cos(2 * radians(GMLS)) - 0.5 * vY * vY * sin(4 * radians(GMLS)) - 1.25 * EEO * EEO * sin(2 * radians(GMAS)))
        return EoT

    def hour_angle_sunrise(SDecline, Lat):
        HASun = degrees(acos(cos(radians(90.833))/(cos(radians(Lat))*cos(radians(SDecline)))-tan(radians(Lat))*tan(radians(SDecline))))
        return HASun

    def solar_noon(EoT, Lon, TimeZone):
        SNoon = (720 - 4 * float(Lon) - float(EoT) + float(TimeZone) * 60) / 1440
        return SNoon

    def sunrise_time(SNoon,HASun):
        SriseTime = (SNoon * 1440 - HASun * 4) / 1440
        return SriseTime

    def sunset_time(SNoon,HASun):
        SsetTime = (SNoon * 1440 + HASun * 4) / 1440
        return SsetTime

    def convert_time_to_seconds(UTC):
        a = 240000 * UTC
        hr_1 = modf(a/10000)[1]
        hr_2 = (modf(a/10000)[0] * 100)/60
        hr = 10000 * (hr_1 + modf(hr_2)[1])
        mn = (modf(((a - hr_1*10000)/100) % 60)[1] + modf(modf(a/100)[0] * 100/60)[1]) *100
        sec = (modf(a/100) %60
        Time = hr + mn + sec
        return Time

    def main(Date,Lat,Lon,TimeZone):
        day = redate(Date)[0]
        month = redate(Date)[1]
        year = redate(Date)[2]
        JD = gregorian_calendar_to_julian_date(year, month, day)
        JC = julian_century(JD)
        GMLS = geometric_mean_longitude_sun(JC)
        GMAS = geometric_mean_anomaly_sun(JC)
        EEO = eccentricity_earth_orbit(JC)
        SEoC = sun_equation_of_center(GMAS, JC)
        STLong = sun_true_longitude(GMLS,SEoC)
        SAL = sun_approximate_longitude(STLong,JC)
        MOE = mean_obliquity_of_ecliptic(JC)
        OC = obliquity_correction(MOE,JC)
        SDecline = sun_declination(SAL,OC)
        vY = varY(OC)
        EoT = equation_of_time(vY,GMLS,EEO,GMAS)
        HASun = hour_angle_sunrise(SDecline,Lat)
        SNoon = solar_noon(EoT,Lon,TimeZone)
        SriseTime = sunrise_time(SNoon,HASun)
        SsetTime = sunset_time(SNoon,HASun)

        RiseSet = [SriseTime, SsetTime]

        return RiseSet
