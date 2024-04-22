from django.test import TestCase

from archive.serealizers import ProcessorSerializer, VideoCardSerializer
from archive.models import Processor, VideoCard, ProcessorBrand, ProcessorModel, Soket, Memory_type


class SerializerTest(TestCase):
    def setUp(self) -> None:
        self.processor_brand_1 = ProcessorBrand.objects.create(name='Intel')
        self.processor_brand_2 = ProcessorBrand.objects.create(name='AMD')
        self.processor_model_1 = ProcessorModel.objects.create(name='i7 7770')
        self.processor_model_2 = ProcessorModel.objects.create(name='Ryzen 5 3600')
        self.soket_1 = Soket.objects.create(name='LGA 1200')
        self.soket_2 = Soket.objects.create(name='AM4')
        self.memory_type_1 = Memory_type.objects.create(name='DDR4')
        self.memory_type_2 = Memory_type.objects.create(name='DDR5')

        # self.videocard

    # TODO дописать тест
    def test_model_processor(self):
        self.processor_1 = Processor.objects.create(brand=self.processor_brand_1,
                                               processor_models=self.processor_model_1,
                                               soket=self.soket_1,
                                               memory_type=self.memory_type_1,
                                               mfs=3200,
                                               tdp=45,
                                               raiting=8000)
        self.processor_2 = Processor.objects.create(brand=self.processor_brand_2,
                                               processor_models=self.processor_model_2,
                                               soket=self.soket_2,
                                               memory_type=self.memory_type_2,
                                               mfs=4800,
                                               tdp=80,
                                               raiting=7000)

        self.assertEqual()
