#Andrew Tan, 2/2, Section 010, Data Size Converter

#Ask user to input file size
size_KB = float(input("Enter a file size, in kilobytes (KB): "))

#Converting and formatting the input
size_B = size_KB * 1024
size_b = size_B * 8
size_MB = size_KB / 1024
size_GB = size_MB / 1024

fsize_B = format(size_B, ">20,.2f")
fsize_b = format(size_b, ">20,.2f")
fsize_MB = format(size_MB, ">20,.2f")
fsize_GB = format(size_GB, ">20,.2f")

print()

#Display converted values in output
print("%.0f KB ..." %(size_KB))

print()

print("... in bits     ", "%s" %(fsize_b), "bits")
print("... in bytes    ", "%s" %(fsize_B), "bytes")
print("... in megabytes", "%s" %(fsize_MB), "MB")
print("... in gigabytes", "%s" %(fsize_GB), "GB")

'''
5 ways to crash
1. syntax error: fsize_B = format(size_B, >20,.2f) [missing quotation marks around the formatting argument]
2. logic error: size_B = size_KB * 1025 [1025 gives the wrong conversion]
3. runtime error: size_MB = size_KB / 0 [division by 0]
4. missing variables fsize_B, fsize_b, fsize_MB, fsize_GB will result in left justified values instead of right justified values
5. size_KB = input("Enter a file size, in kilobytes (KB): ") is missing a float function which will cause the variable to be a string which cannot be mathematically manipulated subsequently
'''
