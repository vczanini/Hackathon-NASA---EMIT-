# Hackathon-NASA---EMIT-
There are several EMIT databases, which can be found using Google Dorking techniques, for example:

</n> --> "emit" + "nasa" or "jpl" + "database" </n>
</n> --> site:github.com + "emit" + "nasa" or "jpl" </n>
</n> --> site:earthdata.nasa.gov + "emit" </n> 

There are raw data extraction methods directly from EMIT or through the official portal, product data. For already recorded mineral dust map projections, there is the L2A technique to download from the "EarthDATA" website. To do this you must download the record, but to have live information you will have to import it into a Python application or a website script with JavaScript, your requirement is to have access to the AWS S3 Access server and insert a temporary access key for 1 hour, obtained by creating the "EarthDATA" account itself.
To download, access the following website and log in: (https://search.earthdata.nasa.gov/search/granules?p=C2408750690-LPCLOUD&pg[0][v]=f&pg[0][gsk]=-start_date&g=G2778173977-LPCLOUD&q=emit&tl=1696639913.466!3!!&lat=-47.546303724069986&long=-163.6875&zoom=0)
