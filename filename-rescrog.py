import os
import shutil

# change to indicate your directory, in which your source and target directories will be located
#
# WARNING: THIS CODE DELETES TARGET DIRECTORY AND ALL ITS CONTENTS IN ORDER TO WRITE TO A
#          FRESH / CLEAN / EMPTY DIRECTORY !!!!!!!!!!!!!!!
#
basePath = 'H:\\_ARCHIVE\\caa\\'
# basePath = '/my/local/path/'

def main():

  sourceDirRoot = basePath + 'bpn'
  targetDirRoot =  basePath + 'bpn-tx'
  # sourceDirRoot = basePath + 'mySourceDirRoot'
  # targetDirRoot =  basePath + 'myTargetDirRoot'

  #
  # here is where code DELETES target dir and re-creates it ... caveat emptor
  #
  if os.path.isdir(targetDirRoot):
    shutil.rmtree(targetDirRoot)
  os.mkdir(targetDirRoot)

  # this code assumes that source files are in directories; directory names will be used
  #  as filename prefixes as files are copied into (flat) target directory ... i.e., target
  #  directory will not contain sub-folders ... code variables suggest that directory names are
  #  dates, but in fact the code will work just as well if they are arbitrary strings
  inputDirectories = os.listdir(sourceDirRoot)
  for item in inputDirectories:
    if os.path.isdir(sourceDirRoot + '\\' + item):
      # print 'directory name: ' + item
      thisSourceDir = sourceDirRoot + '\\' + item
      thisIssueDatePrefix = item
      # print thisIssueDatePrefix
      theseInputFiles = os.listdir(thisSourceDir)
      # print theseInputFiles
      for fileItem in theseInputFiles:
        #
        #
        # this for-loop is specific to patterns of file names in the source directory;
        #  must be changed to fit particular use-cases
        #
        #
        if os.path.isfile(thisSourceDir + '\\' + fileItem):
          filenameBase = fileItem[0:fileItem.find('.')]
          filenameExtension = fileItem[(fileItem.find('.') + 1):]
          # print 'filename base: ' + filenameBase
          # print 'filename extn: ' + filenameExtension
          # print '---'
          thisTargetFileName = ''
          if filenameExtension == 'jpg':
            # code assumes last three characters of filename prior to ".jpg" are a numeral
            #  pattern for which code was originally written assumes that:
            #    filenames whose numeral is 001-004 are page images
            #    filenames whose numeral is 5 are recto images of the front and rear of a single sheet folded 'booklet'
            #    filenames whose numeral is 6 are verso images of the inner pages (2 and 3) of a single sheet folded 'booklet'
            thisPageNumber = filenameBase[(len(filenameBase)-3):]
            if int(thisPageNumber) < 5:
              thisTargetFileName = thisIssueDatePrefix + '_page_' + thisPageNumber + '.jpg'
            elif int(thisPageNumber) == 5:
              thisTargetFileName = thisIssueDatePrefix + '_recto'  + '.jpg'
            elif int(thisPageNumber) == 6:
              thisTargetFileName = thisIssueDatePrefix + '_verso'  + '.jpg'
            else:
              thisTargetFileName = thisIssueDatePrefix + '_ERROR_' + thisPageNumber + '.jpg'
            # print 'filename base: ' + filenameBase
            # print '  page number: ' + thisPageNumber
            # print '  target file: ' + thisTargetFileName
          elif filenameExtension == 'PDF':
            thisTargetFileName = thisIssueDatePrefix + '.PDF'
            # print 'filename base: ' + filenameBase
            # print ' target file: ' + thisTargetFileName
          # print 'source path and filename: ' + thisSourceDir + '\\' + fileItem
          #
          #
          #
          #
          # the print statement below shows the target path and filename w/o doing actual copying
          #  ------
          # uncomment the shutil.copyfile line below to make this script do actual work.....
          #
          #
          print 'target path and filename: ' + targetDirRoot + '\\' + thisTargetFileName
          # shutil.copyfile(thisSourceDir + '\\' + fileItem,targetDirRoot + '\\' + thisTargetFileName)

  return

if __name__ == '__main__':
  main()