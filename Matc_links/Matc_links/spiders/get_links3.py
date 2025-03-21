from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from Matc_links.items import MatcLinksItem

class Matc_links(  scrapy.Spider ):

    name = 'matc_links3'

    allowed_domains = ['madisoncollege.edu']

    start_urls = [
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ACCTG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ADMINPRF/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/AGMECH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ANIM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ANIMTOON/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ANTHRO/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ARABIC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ARCHDR/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ARCHT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ART/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ASTRON/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/AUTMFG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/AUTOBODY/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/AUTOMECH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/AUTOTEC/DEGR",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DENTAST/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DENTHYG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DIESEL/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DIETTEC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DRAMA/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HEALTH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HISTORY/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HORT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HOSPT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HRMGT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HUMSVC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HVAC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HYDPNEU/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BAKING/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BIOLOGY/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BIOTECH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BLCKSMTH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BLDGS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BRCKMSN/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BUSADM/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CABMIL/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CARP/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CHEM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CHINESE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CIVILET/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COLLSUCC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMPABE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMPBSIC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMPSOFT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CONST/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CONSTRTR/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COSMET/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COURT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CPL/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CRIMJUST/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CUL%20ARTS/DEGR",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FARMBUS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FILM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FINANCE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FIRET/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FOODS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FRENCH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FSHNMKTG/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/IND%20MECH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INDMANUF/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INDSGN/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INGOVSRV/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INSMGT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INSTHSKP/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INSURE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/IT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/ITCLOUD/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/ITNET/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/ITPROG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/ITSECUR/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/ITTECSUP/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EARLYCHL/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EARTHSCI/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ECON/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EDSVC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELEC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECENG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECMIC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECSERV/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EMS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENERCONS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENERSVS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENG%20LANG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENGLABE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENGLISH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EVENT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EVTMGT/DEGR",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/L/LABASST/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/L/LANG%20INT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/L/LDRSHP/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/L/LITTRANS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/L/LOGMGT/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MACHT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MASST/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MATH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MATHABE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MCYCLE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MECHDR/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MECTEC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MED%20SUPP/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MEDADMIN/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MEDREC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MEDTERM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MILLWRGT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MKTG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MTLFAB/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MUSIC/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/N/NATSCI/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/N/NONPROFT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/N/NRSAD/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/O/OPTOMET/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/O/ORIENT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/O/OTASST/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PAINTDEC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PARALEG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHARM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHILOS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHOTO/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHOTOVID/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHYED/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHYSICS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PLASTIC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PLASTRDC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PLUMBNG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/POLISCI/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PROF%20DEV/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PRTPUB/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PSYCH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PTASST/DEGR",
"https://my.madisoncollege.edu/app/about"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/RADTEC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/READABE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/READING/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/RECMGT/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/RENEWTHR/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/RESPC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/RLEST/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SCIABE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SHEETMTL/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SMENG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SMLBUS/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SOC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SOCSCABE/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SOCSCI/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SPANISH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SPEECH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/STDNTSUC/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/STEAM/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/STEELIRN/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SUPDEV/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SURGT/DEGR",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/T/T%26D/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/T/TEL%26CBL/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/T/THERMASS/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/V/VETTECH/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/V/VICOM/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GEN%20ST/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GLBL%20ED/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GLBLLANG/DEGR", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GRDSGN/DEGR"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ACCTGFIN/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ANIMTOON/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ART/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/A/ARTS/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BAKING/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BIO%20TECH/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/B/BUS%26MKT/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DENTAL/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DIETMGR/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/D/DRIVED/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CABMIL/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CAREER/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CARP/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CNSTRCT/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMP%20PRO/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMPBSIC/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COMPSOFT/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CONSEC/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COOKING/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/COSMET/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/C/CRIMJUST/NDEG",
"https://my.madisoncollege.edu/app/about"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EARLYCHL/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EB%20TECH/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELEC/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECSERV/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECT/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ELECTRIC/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EMS/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENG%20LANG/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENGLABE/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/ENRICH/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/E/EVENT/NDEG",
"https://my.madisoncollege.edu/app/about"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FAMREL/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FARMBUS/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FIN%20PLAN/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FIRET/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FITNESS/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/F/FOODS/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HEALTH/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HISTORY/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HLTHCARE/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HLTHINTR/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HOME%20DEC/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HOMEINSP/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HOMESHOP/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HORT/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/H/HVAC/NDEG",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INDUSTRY/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/I/INSURE/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GARDEN/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GRAPHIC/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/G/GROUPDYN/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/N/NONPROFT/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/N/NRSAD/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SCIENCE/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SEWFIBER/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SHEETMTL/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/S/SUPRMGMT/NDEG"
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHOTOVID/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PHYED/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PLUMBNG/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PROC%20IMP/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/P/PROF%20DEV/NDEG",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MACHT/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MATHABE/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MCYCLE/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MKTG/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/M/MUSICDNC/NDEG",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/W/WEB%20DSGN/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/W/WELLNESS/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/W/WRITEPUB/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/W/WRLDLANG/NDEG",
"https://my.madisoncollege.edu/app/about",
"https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/READABE/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/REALEST/NDEG", "https://my.madisoncollege.edu/app/catalog/listCoursesBySubject/MATC1/R/RELART/NDEG",
"https://my.madisoncollege.edu/app/about",
]

    def start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpbin( self, response ):

        self.logger.info("Go successful respinse {}".format(response.url))

        items = MatcLinksItem()

        links = response.xpath('*//a/@href').extract()

        items['links'] = links

        yield items


    def errback_httpbin( self,  failure):

        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the non-200 response
        if failure.check(HttpError):

            # These exception come from HttpError spider middleware
            # you can get non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url )

        elif failure.check(DNSLookupError):

            # This is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %', request.url)

        elif failure.check( TimeoutError, TPCTimeOutError ):

            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

        






















